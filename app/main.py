from datetime import datetime  # DO NOT CHANGE THIS IMPORT >:(
from time import sleep


def main() -> None:

    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "a") as file:
            time_string = str(datetime.now())
            file.write(time_string)
            print(f"{time_string} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
