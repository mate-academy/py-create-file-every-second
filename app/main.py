from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}_"
                     f"{datetime.now().minute}_{datetime.now().second}.log")
        with open(f"{file_name}", "w") as f:
            new_line = datetime.now()
            f.write(f"{new_line}")
            print(f"{new_line} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
