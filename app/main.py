from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = str(datetime.now())
        hours = current_time.split()[1][:2]
        minutes = current_time.split()[1][3:5]
        seconds = current_time.split()[1][6:8]
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "x") as time_log:
            time_log.write(f"{current_time}")
        print(current_time, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
