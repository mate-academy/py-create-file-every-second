from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        name = "app-" + time.strftime("%H_%M_%S") + ".log"
        with open(name, "w") as f:
            f.write(str(time))
            print(f"{time} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
