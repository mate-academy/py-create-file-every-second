from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = time_now.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as log:
            log.write(str(time_now))
            print(f"{time_now} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
