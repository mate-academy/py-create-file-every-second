from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = (
            f"app-{time_now.hour}_{time_now.minute}_{time_now.second}.log"
        )
        second_file = open(file_name, "w")
        second_file.write(f"{time_now}")
        print(f"{time_now} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
