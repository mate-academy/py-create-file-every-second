from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def creating_f() -> None:
    date = datetime.now()

    file_name = f"app-{date.hour}_{date.minute}_{date.second}.log"

    timestamp = (f"{date.year}-{date.month}-{date.day} {date.hour}:"
                 f"{date.minute}:{date.second}.{date.microsecond}")

    with open(file_name, "w") as file:
        file.write(timestamp)


def main() -> None:
    while True:
        creating_f()
        sleep(1)


if __name__ == "__main__":
    main()
