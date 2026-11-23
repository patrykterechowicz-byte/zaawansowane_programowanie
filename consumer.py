import argparse
from pathlib import Path
from random import randint
from time import sleep

from task import FileQueue, Status, Task


def parse_args():
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("db_path")
    return parser.parse_args()


def loop(db: FileQueue):
    while True:
        sleep(randint(5, 10))
        task = db.find_pending_task()
        if task is None:
            continue
        db.set_task_status(task, Status.IN_PROGRESS)
        sleep(30)
        db.set_task_status(task, Status.DONE)


if __name__ == "__main__":
    args = parse_args()
    print("Starting consumer.py")
    db = FileQueue(Path(args.db_path))
    try:
        loop(db)
    finally:
        db.close()
