from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hour = str(datetime.now().time().hour)
        minute = str(datetime.now().time().minute)
        second = str(datetime.now().time().second)
        file_name = "app-" + hour + "_" + minute + "_" + second + ".log"
        with open(file_name, "w") as file:
            file.write(str(datetime.now()))
        print(datetime.now(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
