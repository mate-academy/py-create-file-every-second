from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        date_time = datetime.now()
        file_name = (f"app-{date_time.hour}_"
                     f"{date_time.minute}_{date_time.second}.log")
        with open(file_name, "w") as f:
            f.write(str(date_time))
            print(f"{str(date_time)} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
