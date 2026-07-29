from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        time = datetime.now()
        name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(name, "w") as f:
            f.write(str(time))
        sleep(1)
        print(f"{time} {name}")


if __name__ == "__main__":
    main()
