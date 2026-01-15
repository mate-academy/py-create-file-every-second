import time
from datetime import datetime


def main() -> None:
    while True:
        day = datetime.now()
        with open(f"app-{day.hour}_{day.minute}_{day.second}.log",
                  "w") as files:
            files.write(str(datetime.now()))
        print(f"{datetime.now()} app-{day.hour}_{day.minute}_{day.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
