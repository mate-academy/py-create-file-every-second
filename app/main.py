from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        with open(f"app-{date.strftime("%H_%M_%S")}.log", "w") as file:
            file.write(f"{date}")
            print(f"{date} app-{date.strftime("%H_%M_%S")}.log")
        sleep(1)


if __name__ == "__main__":
    main()
