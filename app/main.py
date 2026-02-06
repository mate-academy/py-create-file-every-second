import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        nowstr = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(nowstr + " " + f"app-{now.hour}_{now.minute}_{now.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
