from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        datetime_now = datetime.now()
        hours = datetime_now.hour
        minutes = datetime_now.minute
        seconds = datetime_now.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as file:
            file.write(f"{datetime_now}")
        print(f"{datetime_now} {filename}")
        sleep(1)  # Sleep for 1 second before creating the next log file


if __name__ == "__main__":
    main()
