from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    # write your code here
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        hours, minutes, seconds = now.split(":")

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(str(datetime.now()))
            print(f"{str(datetime.now())} app-{hours}_{minutes}_{seconds}.log")
        sleep(1)


if __name__ == "__main__":
    main()
