from datetime import datetime
from time import sleep


def main() -> None:
    now = datetime.now()
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w") as f:
            f.write(str(now))
            print(now, f"app-{now.hour}_{now.minute}_{now.second}.log")
        sleep(1.0)


if __name__ == "__main__":
    main()
