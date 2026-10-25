import time
from datetime import datetime


def main() -> None:
    while True:
        with open(f"app-{datetime.now().strftime('%H_%M_%S')}.log", "a") as f:
            f.write(datetime.now().
                    strftime("%Y-%m-%d %H:%M:%S"))
            print(f"{datetime.now().
                  strftime('%Y-%m-%d %H:%M:%S app-%H_%M_%S')}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
