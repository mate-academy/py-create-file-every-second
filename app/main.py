from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        with open(
                f"app-{now.hour}_{now.minute}_{now.second}.log", "w"
        ) as file:
            file.write(f"{datetime.now()}")
            print(f"{now} {file.name}")
        sleep(1)


if __name__ == "__main__":
    main()
