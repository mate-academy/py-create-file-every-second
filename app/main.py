from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_part = datetime.now()
        year = time_part.year
        curent_month = time_part.month
        day = time_part.day
        hour = time_part.hour
        minute = time_part.minute
        second = time_part.second

        file_name = f"app-{hour}_{minute}_{second}.log"
        file_stamp = f"{year}-{curent_month}-{day} {hour}:{minute}:{second}"
        with open(file_name, "w") as file:
            file.write(f"{year}-{curent_month}-{day} {hour}:{minute}:{second}")
        print(file_stamp + " " + file_name)
        sleep(1)


if __name__ == "__main__":
    main()
