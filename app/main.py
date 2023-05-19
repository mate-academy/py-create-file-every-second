from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = "app-" + datetime.now().strftime("%H_%M_%S") + ".log"
        with open(file_name, "a") as file_date:
            file_date.write(str(datetime.now()))
        print(f"{datetime.now()} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
