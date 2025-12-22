from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = str(datetime.now())
        file_name = f"app-{date[11:13]}_{date[14:16]}_{date[17:19]}.log"
        with open(file_name, "a") as file:
            file.write(date)
        print(date, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
