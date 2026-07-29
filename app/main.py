import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        name_file = (f"app-"
                     f"{datetime.now().hour}_"
                     f"{datetime.now().minute}_"
                     f"{datetime.now().second}.log")
        log_file = open(f"{name_file}", "w")
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(formatted_time)
        print(f"{formatted_time} {name_file}")
        log_file.close()
        time.sleep(1)


if __name__ == "__main__":
    main()
