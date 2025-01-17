from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S.log")
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(timestamp)
        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
