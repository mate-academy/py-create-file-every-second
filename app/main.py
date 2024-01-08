import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        name = f"app-{date.hour}_{date.minute}_{date.second}.log"
        with open(name, "w") as f:
            f.write(str(date))
        sleep(1)
        print(f"{date} {name}")


if __name__ == "__main__":
    main()
