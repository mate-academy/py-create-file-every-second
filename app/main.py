from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = (
            f"app-{time_now.hour}_{time_now.minute}_{time_now.second}.log"
        )
        time_stamp = time_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as log_file:
            log_file.write(time_stamp)
        print(f"{time_stamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
