from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = datetime.now().strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as current_file:
            current_time = str(datetime.now())
            print(current_time, file_name)
            current_file.write(current_time)
            sleep(1)


if __name__ == "__main__":
    main()
