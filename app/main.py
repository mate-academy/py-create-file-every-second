from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        datetime_format = "app-%H_%M_%S"
        file_append = open(
            f"{datetime.now().strftime(datetime_format)}.log",
            "a")
        datetime_format = "%Y-%m-%d %H:%M:%S"
        file_content = datetime.now().strftime(datetime_format)
        file_append.write(file_content)
        print(file_content + " " + file_append.name)
        sleep(1)


if __name__ == "__main__":
    main()
