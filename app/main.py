import time
from datetime import datetime


def main():
    while True:
        now = datetime.now()
        seconds = now.strftime("%S")
        with open(f"app-{now.hour}_{now.minute}_{seconds}.log", "w") as f:
            f.write(f"{now}")
        print(f"{now} app-{now.hour}_{now.minute}_{seconds}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
