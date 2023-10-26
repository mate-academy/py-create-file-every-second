from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    file_prefix = "app"

    while True:
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (f"{file_prefix}-{current_time.hour}_"
                     f"{current_time.minute}_{current_time.second}.log")

        with open(file_name, "w") as file:
            file.write(timestamp)

        print(timestamp, file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
