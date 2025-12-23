from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as file:
            print(now, file_name)
            file.write(str(now))
        sleep(1)


if __name__ == "__main__":
    main()
