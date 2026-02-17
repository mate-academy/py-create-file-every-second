from datetime import datetime
from time import sleep


def main() -> None:
    """Create one log file per second with timestamp content and print info."""
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(timestamp)

        print(timestamp, filename)
        sleep(1)


if __name__ == "__main__":
    main()
