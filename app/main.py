from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        filename_format = current_time.strftime("app-%H_%M_%S.log")
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(timestamp, filename_format)
        with open(f"{filename_format}", "w") as file:
            file.write(timestamp)
        sleep(1)


if __name__ == "__main__":
    main()
