from datetime import datetime  # DO NOT CHANGE THIS IMPORT

from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()

        hours = current_datetime.hour
        minutes = current_datetime.minute
        seconds = current_datetime.second

        log_filename = f"app-{hours}_{minutes}_{seconds}.log"

        with open(log_filename, "w") as log_file:
            log_file.write(f"{current_datetime}")

        print(f"{current_datetime} {log_filename}")

        sleep(1)


if __name__ == "__main__":
    main()
