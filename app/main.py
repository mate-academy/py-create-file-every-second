from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        with (open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w")
              as file):
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "r") as f:
            print(f.read())
        time.sleep(1)


if __name__ == "__main__":
    main()
