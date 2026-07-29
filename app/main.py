import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date = datetime.now()
        current_date = f"app-{date.hour}_{date.minute}_{date.second}"
        with open(f"{current_date}.log", "w") as f:
            f.write(str(datetime.now()))
            print(f"{datetime.now()} {current_date}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
