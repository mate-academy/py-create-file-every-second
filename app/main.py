from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        file_name = f"app-{date.hour}_{date.minute}_{date.second}.log"
        print(f"{str(date)} {file_name}")
        with open(file_name, "w") as file:
            file.write(str(date))
        sleep(1)


if __name__ == "__main__":
    main()
