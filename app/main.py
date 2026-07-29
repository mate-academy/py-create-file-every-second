from datetime import datetime
from time import sleep


def create_file() -> None:
    now = datetime.now()
    file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "w") as file:
        file.write(timestamp)

    print(f"{timestamp} {file_name}")


def main() -> None:
    while True:
        create_file()
        sleep(1)


if __name__ == "__main__":
    main()
