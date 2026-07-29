import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = now.strftime("app-%H_%M_%S.log")
        with open(filename, "w") as file:
            file.write(f"{timestamp}")
        time.sleep(1)

        print(timestamp, filename)


if __name__ == "__main__":
    main()
