from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        datefmt = "%Y-%m-%d %H:%M:%S"
        file_name = current_time.strftime("app-%H_%M_%S.log")
        line = f"{current_time.strftime(datefmt)}"
        with open(file_name, "w") as file:
            file.write(line)
        print(f"{line} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
