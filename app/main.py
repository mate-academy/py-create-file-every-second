from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        date_time = now.strftime("%H_%M_%S")
        file_name = "app-" + date_time + ".log"
        with open(file_name, "w") as file:
            print(now.strftime("%Y-%m-%d %H:%M:%S"), file_name)
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        sleep(1)


if __name__ == "__main__":
    main()
