import os
import time
from datetime import datetime


def main() -> None:

    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = now.strftime("app-%H_%M_%S.log")
        file_path = os.path.join(os.getcwd(), file_name)

        with open(file_path, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
