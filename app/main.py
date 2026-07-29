from datetime import datetime
from time import sleep
import os


def main() -> None:
    """Run forever, creating timestamped log files every second."""
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Always write file in the current directory
        with open(os.path.join(os.getcwd(), file_name), "w") as f:
            f.write(timestamp)

        # Print confirmation to console
        print(f"{timestamp} {file_name}")

        # Wait one second before next iteration
        sleep(1)


if __name__ == "__main__":
    main()
