from datetime import datetime
from time import sleep


def main():
    while True:
        time = datetime.now()
        with open(f"app-{time.hour}_{time.minute}_{time.second:02d}.log", "w") as f:
            f.write(str(time))
        sleep(1)
        print(f"{time} app-{time.hour}_{time.minute}_{time.second:02d}.log")


if __name__ == "__main__":
    main()
