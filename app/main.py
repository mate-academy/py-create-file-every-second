from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        datetime_now = datetime.now()
        file_name = (f"app-{datetime_now.hour}_"
                     f"{datetime_now.minute}_"
                     f"{datetime_now.second}.log")
        with open(file_name, "w") as file:
            file.write(str(datetime_now))
        print(f"{datetime_now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
