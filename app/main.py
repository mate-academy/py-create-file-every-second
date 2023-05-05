from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        with open(f"app-{datetime.now().hour}"
                  f"_{datetime.now().minute}"
                  f"_{datetime.now().second}.log", "w") as file:
            now = datetime.now()
            file.write(str(now))
            print(str(now), f"app-{now.hour}_{now.minute}_{now.second}.log")
            sleep(1)


if __name__ == "__main__":
    main()
