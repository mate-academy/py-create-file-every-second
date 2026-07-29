from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = time_now.strftime("app-%H_%M_%S.log")
        file_content = time_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(file_content)
            print(f"{file_content} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
