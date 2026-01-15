import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()

        timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

        file_name = (
            f"app-{current_time.hour:02}_"
            f"{current_time.minute:02}_"
            f"{current_time.second:02}.log"
        )

        with open(file_name, "w") as file:
            file.write(timestamp_str)

        print(f"{timestamp_str} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
