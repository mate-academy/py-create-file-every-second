from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        sleep(1)

        date = datetime.now()

        filename = date.strftime("app-%H_%M_%S.log")
        timestamp = date.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {filename}")


if __name__ == "__main__":
    main()
