from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        time = datetime.now()
        seconds = time.second
        minutes = time.minute
        hours = time.hour
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "a") as file:
            file.write(f"{datetime.now()}")
        with open(f"app-{hours}_{minutes}_{seconds}.log", "r") as file:
            print(file.read(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
