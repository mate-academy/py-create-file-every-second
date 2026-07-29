import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_stamp = datetime.now()
        with open(f"app-{time_stamp.hour}_{time_stamp.minute}"
                  f"_{time_stamp.second}.log",
                  "w") as file:
            file.write(f"{time_stamp.year}-{time_stamp.month}"
                       f"-{time_stamp.day} "
                       f"{time_stamp.hour}:{time_stamp.minute}:"
                       f"{time_stamp.second}")
            print(f"{time_stamp} app-{time_stamp.hour}_{time_stamp.minute}"
                  f"_{time_stamp.second}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
