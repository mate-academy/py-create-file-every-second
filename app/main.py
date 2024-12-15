from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        currency_date = datetime.now()
        file_content = str(datetime.now())
        file_name = currency_date.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as file:
            file.write(file_content)
        print(f"{file_content} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
