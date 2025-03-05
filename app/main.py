from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        with open(f"app-{time_now.hour}_"
                  f"{time_now.minute}_"
                  f"{time_now.second}.log", "w") as f:
            f.write(f"{datetime.now()}")
        time.sleep(1)
        print(f"{time_now} app-{time_now.hour}_"
              f"{time_now.minute}_"
              f"{time_now.second}.log")


if __name__ == "__main__":
    main()
