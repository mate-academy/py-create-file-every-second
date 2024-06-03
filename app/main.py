import time
from datetime import datetime


def main() -> None:
    while True:
        datetime_now = datetime.now()
        file_name = f'app-{datetime_now.strftime("%H_%M_%S")}.log'
        timestamp = datetime_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(timestamp)
        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
