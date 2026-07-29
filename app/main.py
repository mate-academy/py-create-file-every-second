from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = now.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as f:
            f.write(timestamp)

        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
