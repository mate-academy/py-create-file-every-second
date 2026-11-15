from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        file_content = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            sleep(1)
            file.write(file_content)
            print(file_content, file_name)


if __name__ == "__main__":
    main()
