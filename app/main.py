from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        with open(f"app-"
                  f"{current_time.hour}_"
                  f"{current_time.minute}_"
                  f"{current_time.second}.log", "w") as log_file:
            log_file.write(str(current_time))
        print(current_time, f"app-{current_time.hour}"
              f"_{current_time.minute}_{current_time.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
