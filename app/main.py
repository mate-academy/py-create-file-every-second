from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        log_file_name = (f"app-{current_time.hour}_"
                         f"{current_time.minute}_{current_time.second}.log")

        with open(log_file_name, "w") as file:
            file.write(str(current_time))

        print(f"{current_time} {log_file_name}")

        time.sleep(1)  # wait for 1 second before creating a new log file


if __name__ == "__main__":
    main()
