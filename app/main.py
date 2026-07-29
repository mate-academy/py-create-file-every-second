from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second

        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        full_file_name = f"app-{hour}_{minute}_{second}.log"
        with open(full_file_name, "w") as file:
            file.write(timestamp)
        print(timestamp, full_file_name)
        sleep(1)


if __name__ == "__main__":
    main()
