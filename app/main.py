from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "a") as new_file:
            new_file.write(f"{now}")
        with open(file_name) as new_file:
            print(new_file.readline(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
