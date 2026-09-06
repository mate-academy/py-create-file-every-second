from datetime import datetime
import time


def main() -> None:
    while True:
        datetime_now = datetime.now()
        timestamp = datetime_now.strftime("%Y-%m-%d %H:%M:%S")
        hours = datetime_now.hour
        minutes = datetime_now.minute
        seconds = datetime_now.second
        print(f"{timestamp} app-{hours}_{minutes}_{seconds}.log")
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(f"{timestamp}")
        time.sleep(1)


if __name__ == "__main__":
    main()
