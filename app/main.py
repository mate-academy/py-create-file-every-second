from datetime import datetime
from time import sleep


def get_timestamp(now: datetime | None = None) -> str:
    now = now or datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def get_file_name(now: datetime | None = None) -> str:
    now = now or datetime.now()
    return f"app-{now.hour}_{now.minute}_{now.second}.log"


def create_file() -> str:
    now = datetime.now()
    timestamp = get_timestamp(now)
    file_name = get_file_name(now)
    with open(file_name, "w") as f:
        f.write(timestamp)
    print(timestamp, file_name)
    return file_name


def main() -> None:
    while True:
        create_file()
        sleep(1)


if __name__ == "__main__":
    main()
