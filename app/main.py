import os
from datetime import datetime
from time import sleep
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> str:
        return self.filename

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


def get_filename(now: datetime) -> str:
    return now.strftime("app-%H_%M_%S.log")


def get_timestamp(now: datetime) -> str:
    return now.strftime("%Y-%m-%d %H:%M:%S")


def main() -> None:
    while True:
        now = datetime.now()
        filename = get_filename(now)
        content = get_timestamp(now)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"{content} {filename}")
        sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess terminated by user. Stopped.")
