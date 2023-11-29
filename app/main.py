from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        data_time = datetime.now()

        file_name = ("app-" + str(data_time.hour)
                     + "_" + str(data_time.minute)
                     + "_" + str(data_time.second)
                     + ".log")

        with open(file_name, "w") as f:
            f.write(str(data_time))
        print(str(data_time), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
