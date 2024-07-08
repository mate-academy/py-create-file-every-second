from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current = datetime.now()
        name = f"app-{current.hour}_{current.minute}_{current.second}.log"
        with open(name, "wt") as f:
            f.write(str(current))
        sleep(1)
        print(current, name)


if __name__ == "__main__":
    main()
