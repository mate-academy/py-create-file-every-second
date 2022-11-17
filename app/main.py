import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        with open(
                f"app-{datetime.now().strftime('%H')}_"
                f"{datetime.now().strftime('%M')}_"
                f"{datetime.now().strftime('%S')}.log",
                "w+") as file:
            now = datetime.now()
            file.write(str(now))
            print(
                f"{str(datetime.now())} app-{datetime.now().strftime('%H')}"
                f"_{datetime.now().strftime('%M')}_"
                f"{datetime.now().strftime('%S')}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
