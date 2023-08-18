from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        filename = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(filename, "w") as file:
            print(time, filename)
            file.write(str(time))
            sleep(1)


if __name__ == "__main__":
    main()
