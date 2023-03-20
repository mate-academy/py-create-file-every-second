from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        file_name = \
            f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"
        with open(file_name, "w") as file:
            print(timestamp, end="", file=file)
        print(timestamp, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
