from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        date = datetime.now()
        file_name = date.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as f:
            f.write(f"{date}")

        print(date, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
