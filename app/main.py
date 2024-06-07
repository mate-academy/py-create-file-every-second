from datetime import datetime
import time


def main() -> None:
    while True:
        current_date_and_time = datetime.now()
        file_name = (f"app-{current_date_and_time.hour}_"
                     f"{current_date_and_time.minute}_"
                     f"{current_date_and_time.second}.log")
        with open(file_name, "w") as file:
            file.write(f"{current_date_and_time}")
            time.sleep(1)
            print(current_date_and_time, file_name)


if __name__ == "__main__":
    main()
