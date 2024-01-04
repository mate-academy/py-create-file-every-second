from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        file_name = f"app-{date.hour}_{date.minute}_{date.second}.log"

        with open(file_name, "w") as file:
            file.write(f"{date.date()} {date.time()}")

        print(f"{date.date()} {date.time()} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
