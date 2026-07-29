from datetime import datetime
from time import sleep
import os


def main() -> None:
    while True:
        cwd = os.getcwd()
        now = datetime.now()
        hour = str(now.hour)
        minute = str(now.minute)
        second = str(now.second)
        current_time = f"app-{hour}_{minute}_{second}.log"
        time = str(now.replace(microsecond=0))
        with open(f"{cwd}/{current_time}", "w") as f:
            f.write(time)
            print(time, current_time)
            sleep(1)


if __name__ == "__main__":
    main()
