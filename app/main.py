from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while ...:
        curr_datetime = datetime.now()
        file_name = curr_datetime.strftime("app-%H_%M_%S.log")

        with open(file_name, "w") as file:
            file.write(str(curr_datetime))
            print(f"{curr_datetime} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
