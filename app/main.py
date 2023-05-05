from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    dt = datetime.now()
    while True:
        with open(f"app-{dt.hour}_{dt.minute}_{dt.second}.log", "w") as f:
            f.write(str(dt))
        print(str(dt) + f" app-{dt.hour}_{dt.minute}_{dt.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
