import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    # write your code here
    while True:
        hours, minutes, seconds = str(datetime.now()).split()[-1].split(":")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(str(datetime.now()))
        with open(file_name, "r") as f:
            print(f.read(), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
