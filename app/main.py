from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        file_name = ("app-"
                     + str(time.hour)
                     + "_" + str(time.minute)
                     + "_" + str(time.second)
                     + ".log")
        with open(file_name, "a") as f:
            f.write(str(time))

        print(time, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
