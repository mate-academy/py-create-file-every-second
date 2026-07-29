from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = now.strftime("app-%H_%M_%S.log")

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(timestamp_str)

        print(f"{timestamp_str} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
