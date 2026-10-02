from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        time_in_format = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(time_in_format)
        print(f"{time_in_format} app-{hours}_{minutes}_{seconds}.log")
        sleep(1)


if __name__ == "__main__":
    main()
