from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        file_name = (f"app-{timestamp.hour}_{timestamp.minute}_"
                     f"{timestamp.second}.log")
        with open(file_name, "w") as date_file:
            date_file.write(str(timestamp))
        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
