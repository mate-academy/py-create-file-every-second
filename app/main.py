from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = f"app-{datetime.now().strftime("%H_%M_%S")}.log"  # noqa: E999
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as log_file:
            log_file.write(f"{time_stamp}")
        print(f"{time_stamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
