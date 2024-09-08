from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        hour = time_now.hour
        minute = time_now.minute
        second = time_now.second
        file_name = f"app-{hour}_{minute}_{second}.log"

        print(f"{time_now} {file_name}")
        log_file = open(file_name, "w")
        log_file.write(f"{time_now}")
        log_file.close()
        time.sleep(1)


if __name__ == "__main__":
    main()
