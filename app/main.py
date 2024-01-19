import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date_and_time = datetime.now()
        hour = date_and_time.hour
        minute = date_and_time.minute
        second = date_and_time.second
        with open(f"app-{hour}_{minute}_{second}.log", "w") as f:
            f.write(str(date_and_time))

        print(f"{date_and_time} app-{hour}_{minute}_{second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
