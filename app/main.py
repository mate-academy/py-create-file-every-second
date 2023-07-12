import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = datetime.now().strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as file:
            file.write(timestamp)
        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
