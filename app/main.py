from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()

        filename = (
            f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"
        )
        timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w", encoding="utf-8") as log_file:
            log_file.write(timestamp_str)

        print(f"{timestamp_str} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
