from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    # write your code here
    while True:
        current_time = datetime.now()
        timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{current_time.hour}_{current_time.minute}_{current_time.second}.log"

        with open(filename, "w") as f:
            f.write(timestamp_str)

        print(f"{timestamp_str} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
