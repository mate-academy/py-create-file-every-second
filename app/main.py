from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        new_file = now.strftime("app-%H_%M_%S.log")

        with open(new_file, "w") as file:
            file.write(timestamp)

            print(f"{timestamp} {new_file}")
            sleep(1)


if __name__ == "__main__":
    main()
