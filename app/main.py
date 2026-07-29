from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_time = datetime.now()
        file_name = (f"app-{date_time.hour}_"
                     f"{date_time.minute}_"
                     f"{date_time.second}.log")
        log_file = open(file_name, "w")
        log_file.write(f"{date_time}")
        log_file.close()
        print(f"{date_time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
