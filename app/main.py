from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        full_date = datetime.now()
        hours = full_date.strftime("%H")
        minutes = full_date.strftime("%M")
        seconds = full_date.strftime("%S")
        with open(f"app-{hours}_{minutes}_{seconds}.log", "a") as file:
            file.write(f"{full_date}")
            print(full_date, file.name)
        sleep(1)


if __name__ == "__main__":
    main()
