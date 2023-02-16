import time
from datetime import datetime


def main() -> None:
    while True:
        with open(f"app-{datetime.now().hour}_{datetime.now().minute}"
                  f"_{datetime.now().second}.log", "w") as f:
            f.write(f"{datetime.now()}")
            print(f"{datetime.now()}", f.name)
            time.sleep(1)


if __name__ == "__main__":
    main()
