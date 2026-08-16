from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = now.strftime("app-%H_%M_%S.log")

        with open(file_name, "w") as file:
            file.write(time)

        print(time, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
