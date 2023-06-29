from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        time_stamp = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(time_stamp, "w") as f:
            f.write(f"{now}")
            print(now, time_stamp)
        time.sleep(1)


if __name__ == "__main__":
    main()
