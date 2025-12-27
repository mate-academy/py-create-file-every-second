from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    def create_a_file() -> None:
        now = datetime.now()
        _file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        _file = open(_file_name, "w")
        _file.write(f"{now}")
        print(f"{now} {_file_name}")
        _file.close()
    create_a_file()
    while True:
        sleep(1)
        create_a_file()


if __name__ == "__main__":
    main()
