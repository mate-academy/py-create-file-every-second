from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep
from types import TracebackType
from typing import Any


class MyContextManager:
    def __init__(
            self,
            filename: str,
            mode: str,
            time_creation: str
    ) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None
        self.time_creation = time_creation

    def __enter__(self) -> Any:
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(
            self,
            exc_type: type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> None:
        print(f"{self.time_creation} {self.filename}")
        self.file.close()


def main() -> None:
    while True:
        now = datetime.now()

        hours = now.hour
        minutes = now.minute
        seconds = now.second

        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with MyContextManager(
                f"app-{hours}_{minutes}_{seconds}.log",
                "w",
                time_creation=timestamp
        ) as context:
            context.write(timestamp)

        sleep(1)


if __name__ == "__main__":
    main()
