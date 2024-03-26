from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        datetime_time = datetime.now()
        current_time = datetime_time.time()
        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_{current_time.second}.log")
        with open(file_name, "w") as f:
            f.write(f"{datetime_time}")
            print(f"{datetime_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
