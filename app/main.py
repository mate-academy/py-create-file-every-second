from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = (f"app-"
                     f"{datetime.now().hour}"
                     f"_{datetime.now().minute}"
                     f"_{datetime.now().second}.log")
        with open(file_name, "w") as file:
            years_month_day_hours_minute_second = datetime.now()
            file.write(f"{years_month_day_hours_minute_second}")
            print(f"{years_month_day_hours_minute_second} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
