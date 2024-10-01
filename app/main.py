import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(timestamp)
        print(f"{timestamp} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
