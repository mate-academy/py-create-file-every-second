import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        datetime_now = datetime.now()
        hours = datetime_now.hour
        minutes = datetime_now.minute
        seconds = datetime_now.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        timestamp = datetime_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(timestamp)
        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
