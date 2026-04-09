import time
from datetime import datetime


def main() -> None:

    while True:
        now = datetime.now()

        filename = now.strftime("app-%H_%M_%S.log")

        timestamp_content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as file:
            file.write(timestamp_content)


        print(f"{timestamp_content} {filename}")

        time.sleep(1)


if __name__ == "__main__":
    main()