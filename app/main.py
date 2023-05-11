import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()

        with open(f"app-{current_time.hour}_"
                  f"{current_time.minute}_"
                  f"{current_time.second}.log", "a") as app_log_file:
            app_log_file.write(str(current_time))
            print(current_time, f"app-{current_time.hour}_"
                                f"{current_time.minute}_"
                                f"{current_time.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
