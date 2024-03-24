from datetime import datetime
from time import sleep


def create_file() -> None:
    now = datetime.now()
    filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
    with open(filename, "w") as f:
        f.write(str(now))
    print(now, filename)


def main() -> None:
    while True:
        create_file()
        sleep(1)


if __name__ == "__main__":
    main()
