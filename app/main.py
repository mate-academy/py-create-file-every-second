from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w+") as file:
            file.write(f"{datetime.now()}")
            file.seek(0)
            print(f"{file.read()} {file.name}")
        sleep(1)


if __name__ == "__main__":
    main()
