from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = now.strftime("app-%H_%M_%S.log")
        with open(filename, "w") as file_:
            file_.write(str(now))

        print(f"{str(now)} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
