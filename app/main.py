from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = str(datetime.now())
        date_list = date.split()
        hours = date_list[1][:2]
        minutes = date_list[1][3:5]
        seconds = date_list[1][6:8]
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        timestamp_file = open(file_name, "w")
        timestamp_file.write(date)
        timestamp_file.close()
        print(f"{date} {file_name}")
        sleep(1)


if __name__ == "__main__":
    pass
