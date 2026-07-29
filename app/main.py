import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        hours, minutes, seconds = (
            current_time.hour,
            current_time.minute,
            current_time.second
        )
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as f:
            f.write(timestamp)

        with open(file_name, "r") as f:
            file_content = f.read()
            print(file_content, file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
