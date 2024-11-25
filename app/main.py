from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while (True):
        with open(f"app-"
                  f"{datetime.now().hour}_{datetime.now().minute}_"
                  f"{datetime.now().second}.log", "w+") as file:
            file.write(str(datetime.now()))
            file.seek(0)
            print(f"{file.read()} {file.name}")

        sleep(1)


if __name__ == "__main__":
    main()
