from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        hours = date.strftime("%H")
        minutes = date.strftime("%M")
        seconds = date.strftime("%S")
        hours = date.hour
        minutes = date.minute
        seconds = date.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(str(date))
            print(str(date), file_name)
            sleep(1)


if __name__ == "__main__":
    main()
