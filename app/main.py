from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S.log")

        with open(file_name, "w") as file:
            file.write(str(now))

        print(f"{str(now)} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
