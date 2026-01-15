from datetime import datetime
import time


def main() -> None:
    while True:
        time_datetime = datetime.now()
        time_time = datetime.now().time()
        with open(f"app-{time_time.hour}_"
                  f"{time_time.minute}_"
                  f"{time_time.second}.log", "w") as file:
            file.write(f"{time_datetime}")
            print(f"{time_datetime} app-{time_time.hour}_"
                  f"{time_time.minute}_"
                  f"{time_time.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
