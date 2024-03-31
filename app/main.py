from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        # Creating file name
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        # Writing new file
        with open(file_name, "w") as new_file:
            new_file.write(str(datetime.now()))

        # Reading file
        with open(file_name, "r") as f:
            print(f.read(), file_name)

        sleep(1)


if __name__ == "__main__":
    main()
