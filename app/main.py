from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()
        current_date = current_datetime.date().strftime("%Y-%m-%d")
        current_time = current_datetime.time().strftime("%H:%M:%S")
        file_name = f"app-{current_datetime.time().strftime("%H_%M_%S")}.log"

        timestamp = f"{current_date} {current_time}"
        with open(file_name, "w") as file:
            file.write(timestamp)
        print(timestamp, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
