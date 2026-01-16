from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        now = datetime.now()
        filename = now.strftime("app-%H_%M_%S.log")
        now = str(now)

        with open(filename, "w") as file:
            file.write(now)
        with open(filename, "r") as file:
            print(file.read() + " " + filename)

        sleep(1)


if __name__ == "__main__":
    main()
