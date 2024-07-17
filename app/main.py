from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        hours = current_date.hour
        minutes = current_date.minute
        seconds = current_date.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as file:
            file.write(str(current_date))
        print(f"{current_date} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
