from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        timestamp = datetime.now()
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (
            f"app-{timestamp.hour}_"
            f"{timestamp.minute}_"
            f"{timestamp.second}.log"
        )
        with open(file_name, "w") as timestamp_file:
            timestamp_file.write(str(formatted_timestamp))
            print(f"{formatted_timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
