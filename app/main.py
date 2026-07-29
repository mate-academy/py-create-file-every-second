from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_datetime = str(datetime.now()).split(".")[0]
        current_time = current_datetime.split()[1]
        file_name = f'app-{current_time.replace(":", "_")}.log'

        with open(f"{file_name}", "w") as date_file:
            date_file.write(current_datetime)

        print(current_datetime, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
