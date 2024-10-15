from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        with open(
            f"app-{datetime.now().hour}_{datetime.now().minute}"
            f"_{datetime.now().second}.log", "w"
        ) as f:
            f.write(str(datetime.now()))
            print(f"{str(datetime.now())} {f.name}")
            sleep(1)


if __name__ == "__main__":
    main()
