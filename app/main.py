from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        log_file_name = (
            f"app-{current_time.hour}_{current_time.minute}"
            f"_{current_time.second}.log"
        )
        with open(log_file_name, "w") as log_file:
            log_file.write(f"{current_time}")
        print(f"{current_time} {log_file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
