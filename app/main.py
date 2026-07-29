import time
from datetime import datetime


def main() -> str:
    while True:
        datetime_per_sec = datetime.now()
        hours = datetime_per_sec.hour
        minutes = datetime_per_sec.minute
        seconds = datetime_per_sec.second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(f"{datetime_per_sec}")
            print(f"{datetime_per_sec} app-{hours}_{minutes}_{seconds}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
