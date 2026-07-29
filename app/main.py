from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        current_time: datetime = datetime.now()

        file_name: str = (
            f"app-{current_time.hour}_{current_time.minute}_"
            f"{current_time.second}.log"
        )

        timestamp: str = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w", encoding="utf-8") as log_file:
            log_file.write(timestamp)

        print(f"{timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
