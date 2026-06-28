from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        date_now = datetime.now()
        file_name = (f"app-{date_now.hour}_"
                     f"{date_now.minute}_{date_now.second}.log")

        with open(file_name, "w") as log_file:
            log_file.write(str(date_now))

        with open(file_name, "r") as log_file:
            print(log_file.read() + " " + file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
