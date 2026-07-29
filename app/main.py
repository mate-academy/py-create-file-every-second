from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current = datetime.now()
        name = f"app-{current.hour}_{current.minute}_{current.second}.log"
        with open(name, "w") as f:
            f.write(f"{current}")
        print(f"{current} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
