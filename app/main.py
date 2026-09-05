from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        create_file()
        sleep(1)


def create_file() -> None:
    datetime_object = datetime.now()
    filename = (
        f"app-{datetime_object.hour}"
        f"_{datetime_object.minute}"
        f"_{datetime_object.second}.log"
    )

    with open(filename, "w") as f:
        f.write(f"{datetime_object}")

    print(f"{datetime_object} {filename}")


if __name__ == "__main__":
    main()
