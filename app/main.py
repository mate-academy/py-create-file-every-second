from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        file_content = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "a") as file:
            file.write(file_content)
        print(f"{file_content} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
