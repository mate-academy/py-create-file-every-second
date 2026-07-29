from time import sleep
from datetime import datetime


def main() -> str:
    while True:
        date = datetime.now()
        with open(f"app-{date.hour}_{date.minute}_{date.second}.log", "a"
                  ) as file:
            file.write(str(date))
            print(date, file.name)
            sleep(1)


if __name__ == "__main__":
    main()
