from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        hours = date.hour
        minutes = date.minute
        seconds = date.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as file:
            file.write(date.strftime("%Y-%m-%d %H:%M:%S"))
            print(date.strftime("%Y-%m-%d %H:%M:%S"), filename)
            sleep(1)


if __name__ == "__main__":
    main()
