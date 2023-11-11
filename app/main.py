from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()

        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second

        filename = f"app-{hours}_{minutes}_{seconds}.log"

        with open(filename, "w") as log_file:
            log_file.write(str(current_time))

        print(current_time, filename)

        time.sleep(1)


if __name__ == "__main__":
    main()
