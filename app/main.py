from datetime import datetime
from time import sleep


def main() -> None:

    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w") as f:
            f.write(date_time)
            print(f"{date_time} {filename}")
            sleep(1)


if __name__ == "__main__":
    main()
