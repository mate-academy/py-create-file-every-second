from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        time = datetime.now()
        name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(name, "w") as f:
            f.write(str(time))

        print(time, name)
        sleep(1)


if __name__ == "__main__":
    main()
