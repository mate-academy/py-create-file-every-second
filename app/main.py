import time
from datetime import datetime


def main() -> None:
    while True:
        try:
            now = datetime.now()
            hours, minutes, seconds = str(now.time()).split(":")
            file_name = (f"app-{hours}_"
                         f"{minutes}_"
                         f"{seconds}")
            with open(f"{file_name}.log", "w") as file:
                file.write(f"{str(now)}")
            print(f"{now} {file_name}.log")
            time.sleep(1)
        except KeyboardInterrupt:
            raise
    pass


if __name__ == "__main__":
    main()
