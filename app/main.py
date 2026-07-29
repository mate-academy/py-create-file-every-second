from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()
        current_datetime_hour = current_datetime.hour
        current_datetime_minute = current_datetime.minute
        current_datetime_second = current_datetime.second

        file_name = (f"app-{current_datetime_hour}_"
                     f"{current_datetime_minute}_"
                     f"{current_datetime_second}.log")
        file_content = f"{current_datetime.__str__()}"

        with open(file_name, "w") as file:
            file.write(file_content)
            print(f"{file_content} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
