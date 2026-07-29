from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = f"{datetime.now()}"
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        sleep(1)
        name = f"app-{hours}_{minutes}_{seconds}.log"
        print(f"{date} {name}")
        with open(name, "w") as f:
            f.write(date)


if __name__ == "__main__":
    main()
