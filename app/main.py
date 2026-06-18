from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (
            f"app-{current_time.hour}_{current_time.minute}_"
            f"{current_time.second}.log"
        )

        print(f"{timestamp} {file_name}")
        with open(file_name, "w") as log_file:
            log_file.write(timestamp)

        sleep(1)


if __name__ == "__main__":
    main()
