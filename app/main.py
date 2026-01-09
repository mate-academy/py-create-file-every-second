from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        get_time = datetime.now()
        with open(f"app-{get_time.hour}_{get_time.minute}_{get_time.second}.log",
                   "w") as outfile:
            outfile.write(str(datetime.now()))
            print(f"{datetime.now()} app-{get_time.hour}_{get_time.minute}_{get_time.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
