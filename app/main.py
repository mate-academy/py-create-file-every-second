from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as f:
            f.write(str(now))
        print(now, filename)
        sleep(1)


if __name__ == "__main__":
    main()
