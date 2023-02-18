from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_time = datetime.now()
        name = date_time.strftime("app-%H_%M_%S")
        with open(f"{name}.log", "a") as file:
            file.write(f"{date_time}")
            print(f"{date_time} {name}.log")
            sleep(1)


if __name__ == "__main__":
    main()
