import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_now = datetime.now()

        hours = time_now.strftime("%H")
        minutes = time_now.strftime("%M")
        seconds = time_now.strftime("%S")
        log_time = time_now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "x") as f:
            f.write(f"{log_time}")
        print(f"{log_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
