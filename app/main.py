from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        filename = (
            f"app-{datetime.now().hour}"
            f"_{datetime.now().minute}"
            f"_{datetime.now().second}")
        with open(filename + ".log", "a") as file:
            file.write(f"{datetime.now()}")
            print(f"{datetime.now()} {filename}.log")
        sleep(1.0)


if __name__ == "__main__":
    main()
