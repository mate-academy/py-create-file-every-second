import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()

        file_name_str = current_time.strftime("%H_%M_%S")
        file_name = ("app-" + file_name_str + ".log")

        log_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(f"{log_time_str}")
            print(f"{log_time_str} {file_name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
