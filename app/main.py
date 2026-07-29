from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        actual_date_time = datetime.now()
        timestamp = str(actual_date_time)
        file_name = ("app-" + timestamp[11:13] + "_" + timestamp[14:16]
                     + "_" + str(int(timestamp[17:19])) + ".log")
        with open(file_name, "w") as f:
            f.write(timestamp)
            print(timestamp + " " + file_name)
        sleep(1)


if __name__ == "__main__":
    main()
