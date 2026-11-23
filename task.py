from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum, auto
import os
from random import randint
import sys
import re
from pathlib import Path
from time import sleep


class Status(StrEnum):
    PENDING = auto()
    IN_PROGRESS = auto()
    DONE = auto()

    @staticmethod
    def from_str(data: str) -> Status:
        match data.strip().lower():
            case "pending":
                return Status.PENDING
            case "in_progress":
                return Status.IN_PROGRESS
            case "done":
                return Status.DONE
            case _:
                raise ValueError(f"Status.from_str got invalid input {data}.")


@dataclass
class Task:
    task_id: int
    status: Status

    @staticmethod
    def from_str(data: str) -> Task:
        words = data.split()
        try:
            task_id = int(words[0])
            status = Status.from_str(words[1])
        except IndexError:
            raise ValueError("Task.from_str assumes len(data.split()) >= 2.")

        return Task(task_id, status)

    def to_str(self) -> str:
        """
        Returns `str` that's guaranteed to be understood by `Task.from_str` method.
        """
        return f"{self.task_id} {self.status}"


class LockExistsError(Exception):
    pass


class FileQueue:
    def __init__(self, path: Path):
        self.db_path: Path = path
        self.__lock_acquired: bool = False

    @property
    def __lock_path(self) -> Path:
        return self.db_path.with_suffix(".lock")

    def __acquire_lock(self):
        if self.__lock_acquired:
            return
        try:
            with open(self.__lock_path, "x") as lock:
                _ = lock.write(str(os.getpid()))
        except FileExistsError:
            raise LockExistsError

        self.__lock_acquired = True

    def __release_lock(self):
        if not self.__lock_acquired:
            pass
        os.remove(self.__lock_path)
        self.__lock_acquired = False

    def close(self):
        """
        If lock is acquired then release it.
        """
        if self.__lock_acquired:
            self.__release_lock()

    def list_tasks(self) -> list[Task]:
        try:
            self.__acquire_lock()
        except LockExistsError:
            sleep(randint(1, 5))
            return self.list_tasks()

        with open(self.db_path) as db:
            lines = db.readlines()
        tasks: list[Task] = []
        for line in lines:
            task = Task.from_str(line)
            tasks.append(task)

        self.__release_lock()
        return tasks

    def find_pending_task(self) -> Task | None:
        tasks = self.list_tasks()
        for task in tasks:
            if task.status == Status.PENDING:
                return task
        return None

    def get_and_start_pending_task(self) -> Task | None:
        """
        Under one lock, finds pending task and starts it. Returns None if no PENDING tasks found.
        """
        try:
            self.__acquire_lock()
        except LockExistsError:
            sleep(randint(1, 5))
            return self.get_and_start_pending_task()

        if not self.db_path.exists():  # no pending tasks
            self.__release_lock()
            return None

        with open(self.db_path, "r") as db:
            lines = db.readlines()

        result = None

        for i, line in enumerate(lines):
            itask = Task.from_str(line)
            if itask.status == Status.PENDING:
                result = Task(itask.task_id, Status.IN_PROGRESS)
                lines[i] = result.to_str() + "\n"
                break

        tmp_db = self.db_path.with_suffix(".tmp")
        with open(tmp_db, "w") as f:
            f.writelines(lines)

        os.replace(tmp_db, self.db_path)

        self.__release_lock()
        return result

    def set_task_status(self, task: Task, new_status: Status):
        try:
            self.__acquire_lock()
        except LockExistsError:
            sleep(randint(1, 5))
            self.set_task_status(task, new_status)
            return

        with open(self.db_path) as db:
            lines = db.readlines()

        for i, line in enumerate(lines):
            itask = Task.from_str(line)
            if itask.task_id == task.task_id:
                lines[i] = Task(itask.task_id, new_status).to_str() + "\n"
                break

        tmp_db = self.db_path.with_suffix(".tmp")
        with open(tmp_db, "w") as f:
            f.writelines(lines)

        os.replace(tmp_db, self.db_path)

        self.__release_lock()

    def new_task(self):
        try:
            self.__acquire_lock()
        except LockExistsError:
            sleep(randint(1, 5))
            self.new_task()
            return

        if not self.db_path.exists():
            self.db_path.touch()

        with open(self.db_path, "r") as db:
            lines = db.readlines()

        top_id = len(lines) + 1

        lines.append(Task(top_id, Status.PENDING).to_str() + "\n")

        tmp_db = self.db_path.with_suffix(".tmp")
        with open(tmp_db, "w") as f:
            f.writelines(lines)

        os.replace(tmp_db, self.db_path)

        self.__release_lock()
