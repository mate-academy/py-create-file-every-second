from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now().strftime("%H_%M_%S")
        current_date = datetime.now().strftime("%Y-%m-%d")

        file_name = "app-" + str(current_time) + ".log"
        file_line = current_date + " " + current_time.replace("_", ":")

        new_file = open(file_name, "w")
        new_file.write(file_line)
        new_file.close()
        print(file_line + " " + file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
