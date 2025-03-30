from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()

        hours = current_datetime.hour
        minutes = current_datetime.minute
        seconds = current_datetime.second

        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as file:
            file.write(str(current_datetime))

        print(current_datetime, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
