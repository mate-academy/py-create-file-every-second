from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        try:
            current_time = datetime.now()
            file_name = (f"app-{current_time.hour}_"
                         f"{current_time.minute}_"
                         f"{current_time.second}.log")

            with open(file_name, "w") as file_log:
                file_log.write(str(current_time))

            print(f"{current_time} {file_name}")
            sleep(1)
        except KeyboardInterrupt:
            raise


if __name__ == "__main__":
    main()
