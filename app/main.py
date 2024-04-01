from datetime import datetime
from time import sleep


def create_log_file() -> str:
    now = datetime.now()
    file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
    with open(file_name, "w") as f:
        f.write(str(now))
    return file_name


def main() -> None:
    while True:
        file_name = create_log_file()
        print(datetime.now(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
