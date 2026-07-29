from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        date_time = datetime.now()
        hours = date_time.hour
        minutes = date_time.minute
        seconds = date_time.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as file:
            file.write(str(date_time))
            print(date_time, file_name)
            time.sleep(1)


if __name__ == "__main__":
    main()
