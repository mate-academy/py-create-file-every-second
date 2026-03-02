import time
from datetime import datetime


def app_hourse_one_sec() -> None:
    while True:
        now = datetime.now()
        file_name = now.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as f:
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            f.write(timestamp)
        print(f"{timestamp} {file_name}")
        time.sleep(1)


def main() -> None:
    app_hourse_one_sec()


if __name__ == "__main__":
    main()
