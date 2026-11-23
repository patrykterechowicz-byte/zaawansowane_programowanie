import argparse
from pathlib import Path

from task import FileQueue, Status, Task


def parse_args():
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("db_path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print("Appending new tasks")
    db = FileQueue(Path(args.db_path))
    db.new_task()
    db.close()
