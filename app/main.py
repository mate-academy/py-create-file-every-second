from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        with open(f"app-{time_now.hour}_"
                  f"{time_now.minute}_"
                  f"{time_now.second}.log", "w") as f:
            print(f"{time_now.strftime("%Y-%m-%d %H:%M:%S")}"
                  f" app-{time_now.hour}_{time_now.minute}_"
                  f"{time_now.second}.log")
            f.write(time_now.strftime("%Y-%m-%d %H:%M:%S"))
        sleep(1)


if __name__ == "__main__":
    main()
