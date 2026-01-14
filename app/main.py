from datetime import datetime  # DO NOT CHANGE THIS IMPORT

import time


def main() -> None:
    while True:
        time_now = datetime.now()
        timestamp = time_now.strftime('%Y-%m-%d %H:%M:%S')
        hours = time_now.strftime('%H')
        minutes = time_now.strftime('%M')
        seconds = time_now.strftime('%S')
        file_name_format = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name_format, "w") as file_every_second:
            file_every_second.write(f"{timestamp}")
            print(f"{timestamp} {file_name_format}")
        time.sleep(1)

if __name__ == "__main__":
    main()
