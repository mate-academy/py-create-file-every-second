from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = time_now.strftime("app-%H_%M_%S.log")
        timestamp = time_now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
