from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        sleep(1)
        file_name = f"app-{time_now.hour}_{time_now.minute}_{time_now.second}"
        with open(f"{file_name}.log", "w") as time_file:
            time_file.write(f"{time_now}")
            print(f"{time_now} {file_name}.log")


if __name__ == "__main__":
    main()
