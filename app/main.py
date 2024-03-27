from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while 1:
        current_datetime = datetime.now()
        hours = current_datetime.hour
        minutes = current_datetime.minute
        seconds = current_datetime.second

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(f"{current_datetime}")
        print(current_datetime, f"app-{hours}_{minutes}_{seconds}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
