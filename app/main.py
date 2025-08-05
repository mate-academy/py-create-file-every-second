from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = datetime.now().strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as f:
            f.write(str(datetime.now()))
            print(datetime.now(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
