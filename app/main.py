from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        timestamp = time_now.strftime("app-%H_%M_%S.log")
        fulldate = time_now.strftime("%Y-%m-%d %H:%M:%S")
        print(fulldate, timestamp)
        with open(timestamp, "w") as f:
            f.write(fulldate)

        sleep(1)


if __name__ == "__main__":
    main()
