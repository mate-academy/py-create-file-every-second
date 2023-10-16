from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()
        file_name = (f"app-{current_datetime.hour:}_"
                     f"{current_datetime.minute}_"
                     f"{current_datetime.second}.log")
        with open(f"{file_name}", "w") as file:
            print(f"{current_datetime} {file_name}")
            file.write(f"{current_datetime}")
        sleep(1)


if __name__ == "__main__":
    main()
