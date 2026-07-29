import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        current_time = datetime.now()
        file_name = (f"app-"
                     f"{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
