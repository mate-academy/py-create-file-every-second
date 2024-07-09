from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now_time = datetime.now()
        file_name = (f"app-{now_time.hour}_"
                     f"{now_time.minute}_"
                     f"{now_time.second}.log")

        with open(file_name, "w") as f:
            f.write(str(now_time))

        print(now_time, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
