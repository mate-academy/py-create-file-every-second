from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now().replace(microsecond=0)
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log",
                  "w",
                  newline="",
                  encoding="utf-8") as f:
            f.write(str(now))

        with open(f"app-{now.hour}_{now.minute}_{now.second}.log",
                  "r",
                  newline="",
                  encoding="utf-8") as f:
            print(f.read(),
                  f"app-{now.hour}_{now.minute}_{now.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
