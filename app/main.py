from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        now = datetime.now()
        file_name = now.strftime("%H_%M_%S")
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"app-{file_name}.log", "w") as second_file:
            second_file.write(timestamp)
            print(timestamp, f"app-{file_name}.log")
            sleep(1)


if __name__ == "__main__":
    main()
