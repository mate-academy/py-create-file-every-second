from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        print(date, f"app-{date.hour}_{date.minute}_{date.second}.log")
        with open(
                file=f"app-{date.hour}_{date.minute}_{date.second}.log",
                mode="w"
        ) as file:
            file.write(str(date))
        sleep(1)


if __name__ == "__main__":
    main()
