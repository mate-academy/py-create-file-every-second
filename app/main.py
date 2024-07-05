import time
from datetime import datetime


def main() -> None:
    while True:
        filename = str(datetime.now()).split(" ")[1].split(":")
        filename = f"app-{filename[0]}_{filename[1]}_{filename[2][:2]}.log"
        with open(filename, "w") as file:
            file.write(str(datetime.now()))
        print(str(datetime.now()), filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
