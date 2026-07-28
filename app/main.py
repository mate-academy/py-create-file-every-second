from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        time = time_now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (f"app-{time_now.hour}_"
                     f"{time_now.minute}_"
                     f"{time_now.second}.log")
        with open(file_name, "w") as log_file:
            log_file.write(time)
            sleep(1)
        print(f"{time} {file_name}")


if __name__ == "__main__":
    main()
