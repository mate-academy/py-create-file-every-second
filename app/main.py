import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        with open(f"app-{datetime.now().hour}_"
                  f"{datetime.now().minute}_"
                  f"{datetime.now().second}.log", "w") as f:
            f.write(f"{datetime.now()}")
            print(f"{datetime.now()}",
                  f"app-{datetime.now().hour}_{datetime.now().minute}"
                  f"_{datetime.now().second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
