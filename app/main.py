from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        name_file = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(name_file, "w") as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"{now} {name_file}")
        sleep(1)


if __name__ == "__main__":
    main()
