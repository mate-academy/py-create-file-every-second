from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        name = (f"app-{datetime.now().hour}_"
                f"{datetime.now().minute}_"
                f"{datetime.now().second}.log")
        created_file = open(name, "w")
        with open(name, "a"):
            line = str(datetime.now())
            created_file.write(line)
            print(f"{line} {name}")
            sleep(1)


if __name__ == "__main__":
    main()
