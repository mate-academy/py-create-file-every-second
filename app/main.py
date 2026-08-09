from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours, minutes, seconds = now.hour, now.minute, now.second

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as log:
            log.write(f"{now:%Y-%m-%d %H:%M:%S}")
        print(f"{now:%Y-%m-%d %H:%M:%S} app-{hours}_{minutes}_{seconds}.log")
        sleep(1)


if __name__ == "__main__":
    main()
