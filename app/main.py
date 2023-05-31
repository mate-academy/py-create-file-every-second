from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()
        hours, minutes, seconds = (
            current_datetime.hour,
            current_datetime.minute,
            current_datetime.second
        )
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as file:
            file.write(f"{datetime.now()}")
        with open(file_name, "r") as file:
            print(f"{file.read()} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
