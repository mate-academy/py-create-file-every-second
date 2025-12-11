from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = "app-" + now.strftime("%H_%M_%S") + ".log"
        log_file = open(file_name, "w")
        log_file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        log_file.close()
        check_file = open(file_name)
        print(f"{check_file.read()} {file_name}")
        check_file.close()
        sleep(1)


if __name__ == "__main__":
    main()
