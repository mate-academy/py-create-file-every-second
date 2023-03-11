from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        date_now = datetime.now()
        file_name = "app-" + str(date_now.hour) + "_" + str(date_now.minute) \
                    + "_" + str(date_now.second) + ".log"
        with open(file_name, "a+") as f:
            f.write(str(date_now))
        print(f"{date_now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
