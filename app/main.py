from datetime import datetime  # DO NOT CHANGE THIS IMPORT

import time


def main() -> None:
    while True:
        data_time_full = datetime.now()

        year = data_time_full.year
        month = data_time_full.month
        day = data_time_full.day

        hour = data_time_full.hour
        minute = data_time_full.minute
        second = data_time_full.second

        file_name = f"app-{hour}_{minute}_{second}.log"
        time_stamp = f"{year}-{month}-{day} {hour}:{minute}:{second}"

        with open(file_name, "w") as file:
            file.write(time_stamp)

        print(f"{year}-{month}-{day} {hour}:{minute}:{second}", file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
