from datetime import datetime
from time import sleep


def main() -> None:
    while True:

        file_name = (
            f"app-{datetime.now().hour}_"
            f"{datetime.now().minute}_"
            f"{datetime.now().second}.log"
        )
        timestamp = str(datetime.now())

        with open(file_name, "w") as new_file:
            new_file.write(timestamp)
        print(timestamp, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
