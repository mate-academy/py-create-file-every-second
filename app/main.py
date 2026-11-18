from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    # Create a file every second
    while True:
        datetime_now = datetime.now()
        file_name = (f"app-{datetime_now.hour}_"
                     f"{datetime_now.minute}_{datetime_now.second}.log")
        with open(file_name, "w") as f:
            f.write(f"{datetime_now}")
        print(f"{datetime_now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
