from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        current_time = datetime.now()

        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        file_new = open(file_name, "w")
        file_new .write(str(current_time))
        file_new .close()
        print(current_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
