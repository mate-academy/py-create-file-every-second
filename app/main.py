from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def create_file() -> str:
    now = datetime.now()
    log_file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
    log_file = open(log_file_name, "w")
    log_file.write(f"{now.year}-{now.month}-{now.day} \
{now.hour}:{now.minute}:{now.second}")
    log_file.close()
    return log_file_name


def read_log_file(log_file_name: str) -> None:
    log_file = open(log_file_name, "r")
    print(f"{log_file.read()} {log_file_name}")
    log_file.close()


def main() -> None:
    while True:
        file_name = create_file()
        read_log_file(file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
