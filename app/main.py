import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w") as f:
            f.write(f"{datetime.now()}")
            print(datetime.now())
        time.sleep(1)


if __name__ == "__main__":
    main()
