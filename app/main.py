from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        today = datetime.now()
        hours = today.hour
        minutes = today.minute
        seconds = today.second
        time_now = f"{hours}:{minutes}:{seconds}"
        current_date = f"{today.year}-{today.month}-{today.day}"
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as file:
            file.write(current_date + " " + time_now)
            print(f"{current_date} {time_now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
