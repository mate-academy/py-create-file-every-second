from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        a = datetime.now()
        d = open(f"app-{a.hour}_{a.minute}_{a.second}.log", "w")
        d.write(f"{a}")
        print(datetime.now(), f"app-{a.hour}_{a.minute}_{a.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
