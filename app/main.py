from datetime import datetime
import time


def main() -> None:
    while True:
        current_datetime = datetime.now()
        hours = current_datetime.hour
        minutes = current_datetime.minute
        seconds = current_datetime.second

        with open(f"app-{hours}_{minutes}_{seconds}.log", "a") as f:
            f.write(f"{datetime.now()}")
            print(datetime.now(), f"app-{hours}_{minutes}_{seconds}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
