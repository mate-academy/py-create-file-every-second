from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        second = datetime.now().second
        minute = datetime.now().minute
        hours = datetime.now().hour
        with open(f"app-{hours}_{minute}_{second}.log",
                  "w", encoding="utf-8") as file:
            file.write(f"{time_now}")
        print(f"{time_now} app-{hours}_{minute}_{second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
