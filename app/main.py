from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_time = datetime.now()
        hours = date_time.hour
        minutes = date_time.minute
        seconds = date_time.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as log_file:
            log_file.write(str(date_time)[:19])
            print(str(date_time)[:19] + " " + file_name)
            sleep(1)


if __name__ == "__main__":
    main()
