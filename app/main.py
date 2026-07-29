from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_time_now: str = datetime.now()
        hours: str = date_time_now.hour
        minutes: str = date_time_now.minute
        seconds: str = date_time_now.second
        filename: str = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as file:
            print(date_time_now, filename)
            file.write(date_time_now.strftime("%Y-%m-%d %H:%M:%S"))
        sleep(1)


if __name__ == "__main__":
    main()
