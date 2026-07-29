from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        file_info = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(file_info)
            print(file_info, file_name)
            sleep(1)


if __name__ == "__main__":
    main()
