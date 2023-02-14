from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        with open(
                f"app-{date.hour}_{date.minute}_{date.second}.log", "w"
        ) as file:
            print(
                str(date), f"app-{date.hour}_{date.minute}_{date.second}.log"
            )
            file.write(str(date))
        sleep(1)


if __name__ == "__main__":
    main()
