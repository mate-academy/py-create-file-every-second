from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w") as f:
            f.write(now.__str__())
        with open(filename, "r") as f:
            print(f.read(), filename)
        sleep(1)


if __name__ == "__main__":
    main()
