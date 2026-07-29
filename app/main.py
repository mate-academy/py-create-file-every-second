import time
from datetime import datetime


def main() -> None:
    while True:
        current_datetime = datetime.now()
        hours = current_datetime.hour
        minutes = current_datetime.minute
        seconds = current_datetime.second

        log_filename = f"app-{hours}_{minutes}_{seconds}.log"
        log_content = str(current_datetime)

        with open(log_filename, "w") as file:
            file.write(log_content)

        print(f"{log_content} {log_filename}")

        time.sleep(1)


if __name__ == "__main__":
    main()
