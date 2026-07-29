import time
from datetime import datetime


def main() -> None:
    while True:
        time_now = datetime.now()
        with open(f"app-{time_now.hour}_"
                  f"{time_now.minute}_{time_now.second}.log", "a") as f:
            f.write(str(time_now))
            print(str(time_now),
                  f"app-{time_now.hour}_"
                  f"{time_now.minute}_{time_now.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
