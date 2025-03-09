import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        with open(
            f"app-{int(datetime.now().strftime('%H'))}_"
            f"{int(datetime.now().strftime('%M'))}_"
            f"{int(datetime.now().strftime('%S'))}.log", "w"
        ) as log:
            log.write(f"{str(datetime.now())}")
            print(f"{str(datetime.now())} "
                  f"app-{int(datetime.now().strftime('%H'))}_"
                  f"{int(datetime.now().strftime('%M'))}_"
                  f"{int(datetime.now().strftime('%S'))}.log")

        time.sleep(1)


if __name__ == "__main__":
    main()
