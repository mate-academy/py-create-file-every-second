from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    # write your code here
    while True:
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{current_time.hour}_{current_time.minute}_"
        filename += f"{current_time.second}.log"
        with open(filename, "w") as log_file:
            log_file.write(timestamp)
        print(f"{timestamp} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
