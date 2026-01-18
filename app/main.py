import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = str(datetime.now()).split()[1].split(".")[0].split(":")
        hours = current_time[0]
        minutes = current_time[1]
        seconds = current_time[2]
        with open(f"app/app-{hours}_{minutes}_{seconds}.log", "w"):
            time.sleep(1)


if __name__ == "__main__":
    main()
