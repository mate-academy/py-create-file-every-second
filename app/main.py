from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        file_time_now = open(
            f"app-{time_now.hour}_{time_now.minute}_{time_now.second}.log",
            "w",
        )
        file_time_now.write(str(time_now))
        print(
            str(time_now),
            f"app-{time_now.hour}_{time_now.minute}_{time_now.second}.log",
        )
        time.sleep(1)


if __name__ == "__main__":

    main()
