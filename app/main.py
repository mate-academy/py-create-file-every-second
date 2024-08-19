from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_stamp = datetime.now()
        sleep(1)
        file_name = (
            "app-"
            + str(date_stamp.hour)
            + "_" + str(date_stamp.minute)
            + "_" + str(date_stamp.second)
            + ".log"
        )

        print_string = str(date_stamp) + " " + file_name

        try:
            with open(file_name, "w") as fo:
                fo.write(str(date_stamp))
        except KeyboardInterrupt:
            break

        print(print_string)


if __name__ == "__main__":
    main()
