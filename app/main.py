from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_time = datetime.now()
        file_name = date_time.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as f:
            f.write(str(date_time))
            print(date_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
