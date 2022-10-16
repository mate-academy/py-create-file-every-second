from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


class FileManager:
    def __init__(self) -> None:
        self.mode = "a+"
        self.file = None

    def __enter__(self) -> object:
        hour = f"{datetime.now()}"[11:13]
        minutes = f"{datetime.now()}"[14:16]
        seconds = f"{datetime.now()}"[17:19]
        self.name = f"app-{hour}_{minutes}_{seconds}.log"
        self.file = open(self.name, self.mode)
        print(datetime.now(), self.name)
        return self.file

    def __exit__(self, exc_type: str, exc_val: int, exc_tb: str) -> None:
        self.file.close()


def main() -> None:
    while True:
        with FileManager() as f:
            f.write(f"{datetime.now()}")
            sleep(1)


if __name__ == "__main__":
    main()
