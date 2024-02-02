from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()
        file_name = f"app-{current_datetime.strftime('%H_%M_%S')}.log"

        with open(file_name, "w") as file:
            file.write(f"{current_datetime.strftime("%Y-%m-%d %H:%M:%S")}")

        with open(file_name, "r") as file:
            text = file.read()
            print(f"{text} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
