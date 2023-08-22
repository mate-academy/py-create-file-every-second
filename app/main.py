from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        name = f"app-{datetime.now().hour}_{datetime.now().minute}" \
               f"_{datetime.now().second}.log"
        with open(name, "w") as f:
            f.write(str(datetime.now()))
            print(datetime.now(), name)
            sleep(1)


if __name__ == "__main__":
    main()
