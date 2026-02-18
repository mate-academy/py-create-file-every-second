from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def create_log_file(now: datetime) -> str:
    """
    Creates a log file with the required name and content.
    Returns the file name.
    """
    filename: str = f"app-{now.hour}_{now.minute}_{now.second}.log"
    timestamp: str = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w") as f:
        f.write(timestamp)

    return filename


def main() -> None:
    while True:
        now: datetime = datetime.now()

        filename: str = create_log_file(now)
        timestamp: str = now.strftime("%Y-%m-%d %H:%M:%S")

        print(f"{timestamp} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
