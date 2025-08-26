from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_data = str(datetime.now())
        hours, minutes, seconds, *_ = str(date_data).split(" ")[1].split(":")
        seconds = seconds.split(".")[0]
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as file:
            file.write(date_data.split(".")[0])
        sleep(1)

        print(f'{date_data.split(".")[0]} {file_name}')


if __name__ == "__main__":
    main()
