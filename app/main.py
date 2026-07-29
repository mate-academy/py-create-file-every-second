from datetime import datetime
from time import sleep


def main() -> datetime:
    current_time = datetime.now()
    while True:
        sleep(1)
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(f"{current_time}")
        hh = f"{current_time} app-{hours}_{minutes}_{seconds}.log"
        print(hh)
        current_time = datetime.now()


if __name__ == "__main__":
    main()
