from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        file_name = get_file_name(now)
        formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(formatted_date_time)

            print(f"{formatted_date_time} {file_name}")

        sleep(1)


def get_file_name(now: datetime) -> str:
    return f"app-{now.hour}_{now.minute}_{now.second}.log"


if __name__ == "__main__":
    main()
