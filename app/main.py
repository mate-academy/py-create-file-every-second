from datetime import datetime
from time import sleep


def create_file() -> None:
    now = datetime.now()
    file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
    file_content = f"{now} {file_name}\n"

    with open(file_name, "w") as file:
        file.write(str(now))
    print(file_content, end="")


def main() -> None:
    while True:
        create_file()
        sleep(1)


if __name__ == "__main__":
    main()
