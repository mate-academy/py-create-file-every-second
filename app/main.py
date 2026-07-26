from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        date_str = f"{time_now.strftime('%Y-%m-%d %H:%M:%S')}"
        log_file_name = f"{time_now.strftime('app-%H_%M_%S.log')}"
        with open(log_file_name, "w") as log_file:
            log_file.write(f"{date_str}")
        print(date_str, log_file_name)
        sleep(1)


if __name__ == "__main__":
    main()
