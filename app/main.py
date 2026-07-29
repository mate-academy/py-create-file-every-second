from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_stamp = datetime.now()
        file_name = (f"app-{time_stamp.hour}_"
                     f"{time_stamp.minute}_"
                     f"{time_stamp.second}.log")

        with open(file_name, "a") as f:
            f.write(str(time_stamp))

        print(f"{time_stamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
