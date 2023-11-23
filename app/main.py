from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_now = datetime.now()
        file_name = (f"app-{date_now.hour}"
                     f"_{date_now.minute}_"
                     f"{date_now.second}.log")
        with open(file_name, "w") as record:
            record.write(str(date_now))
            print(f"{str(date_now)} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
