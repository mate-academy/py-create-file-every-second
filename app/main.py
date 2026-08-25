from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = datetime.now().strftime("app-%H_%M_%S.log")
        file_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(file_content)
        print(file_content, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
