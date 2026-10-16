from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}_{datetime.now().minute}"
                     f"_{datetime.now().second}.log")
        with open(file_name, "a") as f:
            f.write(f"{datetime.now()}")
            print(f"{str(datetime.now())} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
