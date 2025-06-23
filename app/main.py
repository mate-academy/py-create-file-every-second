from datetime import datetime
from time import sleep


def main():
    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S.log")

        with open(file_name, "w") as file:
            file.write(f"{now}\n")

        print(f"{now} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
