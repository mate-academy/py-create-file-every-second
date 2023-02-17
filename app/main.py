from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_stamp = datetime.now()
        file_name = (
            f"app-{date_stamp.hour}_{date_stamp.minute}_"
            f"{date_stamp.second}.log"
        )
        with open(file_name, "w") as fw:
            fw.write(str(date_stamp))
        print(date_stamp, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
