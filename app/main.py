from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    time_format: str = "%H_%M_%S"
    while True:
        current_time: datetime = datetime.now()
        file_name: str = f"app-{current_time.strftime(time_format)}.log"

        with open(file_name, "w") as file:
            file.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))

        print(f"{current_time.strftime("%Y-%m-%d %H:%M:%S")} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
