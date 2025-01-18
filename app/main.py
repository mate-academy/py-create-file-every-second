from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()
        file_name = current_datetime.strftime("app-%H_%M_%S.log")

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(str(current_datetime))

        print(f"{current_datetime} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
