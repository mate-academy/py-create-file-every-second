import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as f:
            timestamp = (str(datetime.now()))
            f.write(timestamp)
        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
