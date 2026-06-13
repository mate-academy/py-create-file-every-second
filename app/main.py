from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        # Get current timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Build file name: app-{hours}_{minutes}_{seconds}.log
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Write timestamp to file in current working directory
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(timestamp)

        # Print to console
        print(f"{timestamp} {file_name}")

        # Sleep for 1 second
        sleep(1)


if __name__ == "__main__":
    main()
