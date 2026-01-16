from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        file_name = current_date.strftime("app-%H_%M_%S.log")
        file_content = str(current_date)
        with open(file_name, "w") as file:
            file.write(file_content)
        print(f"{current_date} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
