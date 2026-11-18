from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = datetime.now().strftime("app-%H_%M_%S.log")
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "a") as f:
            f.write(time_now)
        print(f"{time_now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
