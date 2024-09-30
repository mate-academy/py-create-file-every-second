from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:git
    while True:
        current_date = datetime.now()
        file_name = ("app-" + str(current_date.hour)
                     + "_" + str(current_date.minute)
                     + "_" + str(current_date.second)
                     + ".log")
        print(f"{str(current_date)} {file_name}")
        with open(file_name, "w") as new_file:
            new_file.write(str(current_date))
        time.sleep(1)


if __name__ == "__main__":
    main()
