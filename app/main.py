from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}_"
                     f"{datetime.now().minute}_"
                     f"{datetime.now().second}"
                     )
        with open(file_name + ".log", "w") as file:
            file.write(str(datetime.now()))
            print(f"{datetime.now()} {file_name}.log")
        sleep(1)


if __name__ == "__main__":
    main()
