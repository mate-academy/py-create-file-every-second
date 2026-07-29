from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "a") as f:
            f.write(str(now))
            sleep(1)
            print(now, f"app-{now.hour}_{now.minute}_{now.second}.log")


if __name__ == "__main__":
    main()
