from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_datetime = str(datetime.now())
        file_name = "app-" + "_".join(current_datetime[11:21].split(":")) +\
                    ".log"
        with open(file_name, "w") as file:
            file.write(current_datetime[:21])
        print(current_datetime[:21] + " " + file_name)
        sleep(1)


if __name__ == "__main__":
    main()
