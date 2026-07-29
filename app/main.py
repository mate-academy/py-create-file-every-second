from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = now.strftime("app-%H_%M_%S.log")

        with open(filename, "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        print(now.strftime("%Y-%m-%d %H:%M:%S"), filename)
        sleep(1)


if __name__ == "__main__":
    main()
