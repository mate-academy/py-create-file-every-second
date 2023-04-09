from time import sleep
from datetime import datetime
from typing import TextIO


def main() -> None:
    class FileManager:
        def __init__(self, filename: str, mode: str) -> None:
            self.filename = filename
            self.mode = mode

        def __enter__(self) -> TextIO:
            self.file = open(self.filename, self.mode)
            return self.file

        def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
            self.file.close()

    while True:
        h_now = datetime.now().hour
        min_now = datetime.now().minute
        sec_now = datetime.now().second
        time_now = datetime.now()
        file_name = f"app-{h_now}_{min_now}_{sec_now}.log"
        with FileManager(file_name, "w") as f:
            f.write(str(time_now))
        print(time_now, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
