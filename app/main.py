from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        year = current_time.year
        month = current_time.month
        day = current_time.day
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        file_name = f"app-{hours:02d}_{minutes:02d}_{seconds}.log"
        with open(file_name, "w") as file:
            file.write(f"{year}-{month:02d}-{day:02d} "
                       f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        print(f"{year}-{month:02d}-{day:02d} "
              f"{hours:02d}:{minutes:02d}:{seconds:02d} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
