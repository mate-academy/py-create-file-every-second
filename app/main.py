from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        curr_time = datetime.now()
        file_name = (f"app-{curr_time.hour}_"
                     f"{curr_time.minute}_"
                     f"{curr_time.second}.log")

        log_file = open(file_name, "w")
        log_file.write(f"{curr_time}")
        log_file.close()
        print(datetime.now(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
