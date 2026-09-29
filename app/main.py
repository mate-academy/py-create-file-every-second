from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        filename = (
            f"app-{timestamp.hour}_{timestamp.minute}_"
            f"{timestamp.second}.log"
        )

        with open(filename, "w") as log_file:
            log_file.write(formatted_timestamp)

        print(f"{formatted_timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
