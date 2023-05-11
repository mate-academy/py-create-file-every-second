import time
from datetime import datetime


def main() -> None:
    while True:
        current_date = datetime.now()
        formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S.%f")
        file_name = "app-" + current_date.strftime("%H_%M_%S") + ".log"
        with open(file_name, "a") as f:
            f.write(formatted_datetime)
            print(formatted_datetime, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
