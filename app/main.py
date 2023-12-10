from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_now = datetime.now()
        name_file = (f"app-{date_now.hour}_"
                     f"{date_now.minute}_{date_now.second}.log")
        with open(name_file, "w") as file:
            file.write(f"{date_now}")
        print(f"{date_now} {name_file}")
        sleep(1)


if __name__ == "__main__":
    main()
