from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour:02d}_{now.minute:02d}_{now.second:02d}.log"
        with open(filename, "w") as f:
            f.write(str(datetime.now()))
            print(str(datetime.now()) + " " + filename)
        sleep(1)


if __name__ == "__main__":
    main()
