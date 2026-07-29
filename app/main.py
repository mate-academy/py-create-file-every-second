import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        with open(f"app-{hour}_{minute}_{second}.log", "w") as f:
            time_now = datetime.now()
            f.write(f"{time_now}")
            print(time_now, f"app-{hour}_{minute}_{second}.log")
        time.sleep(1.0)


if __name__ == "__main__":
    main()
