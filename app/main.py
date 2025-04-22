from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.hour}-{current_time.minute}-{current_time.second}.log"
        timestamp_content = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(timestamp_content)
        sleep(1)


if __name__ == "__main__":
    main()
