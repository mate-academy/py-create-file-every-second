from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        time_hours_min_sec = date.strftime("%H_%M_%S")
        with open(f"app-{time_hours_min_sec}.log", "w") as file:
            file.write(f"{date}")
            print(f"{date} app-{time_hours_min_sec}.log")
        sleep(1)


if __name__ == "__main__":
    main()
