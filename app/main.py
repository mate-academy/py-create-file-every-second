from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        date = datetime.now()
        time_stamp = date.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{date.strftime("%H_%M_%S")}.log"
        one_log = f"{time_stamp} {file_name}"
        with open(f"{file_name}", "a") as file:
            file.write(f"{time_stamp}")
        print(one_log)
        sleep(1)


if __name__ == "__main__":
    main()
