from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        timestamp = str(datetime.now())
        file_name = datetime.now().strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as config_file:
            config_file.write(timestamp)
        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
