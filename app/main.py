from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        hours = time_now.hour
        minutes = time_now.minute
        seconds = time_now.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as log_file:
            log_file.write(str(time_now))
        print(time_now, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
