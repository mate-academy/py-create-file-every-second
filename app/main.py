from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log",
                  "w") as file:
            print(str(datetime.now())[:19],
                  f"app-{now.hour}_{now.minute}_{now.second}.log")
            file.write(str(datetime.now())[:19])
        sleep(1)


if __name__ == "__main__":
    main()
