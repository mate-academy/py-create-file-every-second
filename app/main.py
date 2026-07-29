from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second
        file_name = f"app-{hour}_{minute}_{second}.log"
        timestamp = str(current_time)

        with open(file_name, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
