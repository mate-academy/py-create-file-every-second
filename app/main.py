from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_ = datetime.now()
        file_name = f"app-{time_.hour}_{time_.minute}_{time_.second}.log"
        with open(file_name, "w") as file:
            file.write(str(time_))
            print(time_, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
