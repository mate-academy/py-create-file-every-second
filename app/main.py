import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = now.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as file:
            file.write(timestamp)
        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
