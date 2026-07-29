from datetime import datetime
from time import sleep


def creating_file() -> None:

    date = datetime.now()
    file_name = f"app-{date.hour}_{date.minute}_{date.second}.log"
    timestamp = str(datetime.now())

    with open(file_name, "w") as file:
        file.write(timestamp)

    print(f"{date} {file_name}")


def main() -> None:
    while True:
        creating_file()
        sleep(1)


if __name__ == "__main__":
    main()
