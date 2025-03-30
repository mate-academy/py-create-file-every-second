from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        with open(
                f"app-{time.hour}_{time.minute}_{time.second}.log", "a"
        ) as file:
            file.write(f"{time}")
            print(f"{time} app-{time.hour}_{time.minute}_{time.second}.log")
            sleep(1)


if __name__ == "__main__":
    main()
