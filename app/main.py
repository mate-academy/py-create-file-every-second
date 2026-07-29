from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        name_file = f"app-{hours}_{minutes}_{seconds}.log"
        with open(name_file, "w") as file:
            now = datetime.now()
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(now.strftime("%Y-%m-%d %H:%M:%S"), name_file)
        sleep(1)


if __name__ == "__main__":
    main()
