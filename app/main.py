from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        hours = time_now.hour
        minutes = time_now.minute
        seconds = time_now.second
        date = time_now.date()
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        timestamp = f"{date} {hours}" + ":" + f"{minutes}" + ":" + f"{seconds}"
        with open(filename, "w") as f:
            f.write(timestamp)
            print(f"{timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
