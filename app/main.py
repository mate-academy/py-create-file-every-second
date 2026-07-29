from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as file:
            file.write(str(current_time))
        print(current_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
