import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = str(datetime.now()).split(" ")[1].split(".")[0].split(":")
        hours, minutes, seconds = now
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as file:
            file.write(str(datetime.now()))
            print(str(datetime.now()) + " " + file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
