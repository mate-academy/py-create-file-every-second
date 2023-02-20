from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:

    while True:
        now = datetime.now()
        my_file = open(f"app-{now.hour}_{now.minute}_{now.second}.log", "a")
        print(now, f"app-{now.hour}_{now.minute}_{now.second}.log")
        my_file.write(f"{now}")
        my_file.close()
        time.sleep(1)


if __name__ == "__main__":
    main()
