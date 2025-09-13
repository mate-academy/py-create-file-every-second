from datetime import datetime
from time import sleep


def main() -> None:

    while True:
        date = datetime.now()
        filename = f"app-{date.hour}_{date.minute}_{date.second}.log"
        with open(filename, "w") as file:
            file.write(str(date))
            print(str(date), filename)
        sleep(1)


if __name__ == "__main__":
    main()
