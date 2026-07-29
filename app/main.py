import time
from datetime import datetime


def main() -> None:
    while True:
        date = str(datetime.now())
        hours = date[11: 13]
        minutes = date[14: 16]
        seconds = date[17: 19]
        name_of_the_file = f"app-{hours}_{minutes}_{seconds}.log"
        with open(name_of_the_file, "w") as file:
            file.write(f"{date}")
            print(date + " " + name_of_the_file)
            time.sleep(1)


if __name__ == "__main__":
    main()
