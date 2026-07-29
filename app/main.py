from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    """
    Create a log file every second with the current timestamp.
    The file name follows the format 'app-H_M_S.log' and the content includes
    the full date and time (YYYY-MM-DD HH:MM:SS).
    """
    while True:
        get_time = datetime.now()
        ts_str = get_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{get_time.hour}_{get_time.minute}_{
            get_time.second}.log"

        with open(file_name, "w") as file:
            file.write(ts_str)
            print(ts_str, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
