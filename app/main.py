from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        filename = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(filename, "w") as f:
            f.write(str(time))
        print(time, filename)
        sleep(1)


if __name__ == "__main__":
    main()
