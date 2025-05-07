import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        time_now = datetime.now()
        timestamp = time_now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = time_now.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as f:
            f.write(f"{timestamp}")

        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
