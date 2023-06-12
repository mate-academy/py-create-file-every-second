from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_date_time = datetime.now()
        current_hour = current_date_time.time().hour
        current_minute = current_date_time.time().minute
        current_second = current_date_time.time().second
        file_name = f"app-{current_hour}_{current_minute}_{current_second}.log"
        with open(file_name, "w") as new_file:
            new_file.write(str(current_date_time))
            print(current_date_time, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
