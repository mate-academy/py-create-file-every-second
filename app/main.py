from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(str(datetime.now()))
            print(str(datetime.now()), file.name)
        sleep(1)


if __name__ == "__main__":
    main()
