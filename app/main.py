from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        data_string = str(datetime.now())
        file_name = "app-" + data_string[11:19].replace(":", "_") + ".log"
        with open(file_name, "w") as file:
            file.write(data_string)
            print(data_string + " " + file.name)
        sleep(1)


if __name__ == "__main__":
    main()
