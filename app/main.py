from time import sleep
from datetime import datetime


def main():
    while True:
        now = datetime.now()
        hours, minutes, seconds = now.hour, now.minute, now.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        with open(filename, "r") as f:
            print(f.read(), filename)
        sleep(1)


if __name__ == "__main__":
    main()
