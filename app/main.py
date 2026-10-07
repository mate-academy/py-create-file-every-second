from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()
        file_name = (f"app-{current_datetime.hour}_"
                     f"{current_datetime.minute}_"
                     f"{current_datetime.second}.log")

        with open(file_name, "w") as file:
            timestamp = str(current_datetime)[:19]
            file.write(timestamp)

        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
