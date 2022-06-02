from datetime import datetime
from time import sleep


def main():
    while True:
        file_name = datetime.now().strftime("app-%H_%M_%S.log")
        file_content = str(datetime.now())

        with open(file_name, "w") as f:
            f.write(file_content)

        with open(file_name, "r") as f:
            print(f"{f.read()} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
