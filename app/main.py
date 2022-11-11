import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        with open(f"app-{datetime.now().strftime('%H_%M_%#S')}.log", "w+")\
                as f:
            f.write(f"{datetime.now()}")
            with open(f"app-{datetime.now().strftime('%H_%M_%#S')}.log", "r")\
                    as f:
                f.read()
            print(f"{datetime.now()} app"
                  f"-{datetime.now().strftime('%H_%M_%#S')}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
