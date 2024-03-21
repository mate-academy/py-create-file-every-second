from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        datetime_now = datetime.now()
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as file:
            file.write(str(datetime_now))

            print(f"{datetime_now} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
