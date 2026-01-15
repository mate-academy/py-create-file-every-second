from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    # write your code here
    while True:
        current = datetime.now()
        fname = f"app-{current.hour}_{current.minute}_{current.second}.log"
        with open(fname, "a") as f:
            f.write(current.__str__())
        sleep(1)
        print(current.__str__(), fname)


if __name__ == "__main__":
    main()
