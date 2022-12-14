from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep, strftime


def main() -> None:
    while True:
        current_date = datetime.now()
        file_name = strftime(f"app-{current_date.hour}_"
                             f"{current_date.minute}_"
                             f"{current_date.second}.log")
        with open(file_name, "w") as new_file:
            new_file.write(str(current_date))
            print(datetime.now(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
