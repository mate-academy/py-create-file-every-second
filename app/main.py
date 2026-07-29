from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        date = datetime.now()
        name_of_file = f"app-{date.hour}_{date.minute}_{date.second}.log"
        with open(name_of_file, "w") as f:
            f.write(str(date))
            print(f"{date} {name_of_file}")
        sleep(1)


if __name__ == "__main__":
    main()
