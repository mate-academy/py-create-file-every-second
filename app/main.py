from datetime import datetime
from time import sleep


def create_log_file() -> None:
    current_time = datetime.now()

    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    file_name = (
        f"app-{current_time.hour}_"
        f"{current_time.minute}_"
        f"{current_time.second}.log"
    )

    with open(file_name, "w") as file:
        file.write(timestamp)

    print(f"{timestamp} {file_name}")


def main() -> None:
    while True:
        create_log_file()
        sleep(1)


if __name__ == "__main__":
    main()
