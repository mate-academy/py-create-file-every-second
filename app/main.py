from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        file_name = (f"app-{date.hour}_"
                     f"{date.minute}_"
                     f"{date.second}.log")
        date_in_file = date.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(date_in_file)
        print(f"{date_in_file} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
