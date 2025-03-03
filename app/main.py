from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = now.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as f:
            f.write(time_stamp)
        print(f"{time_stamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
