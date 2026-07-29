from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(f"{name}", "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
            print(now.strftime("%Y-%m-%d %H:%M:%S") + " " + name)
        sleep(1)


if __name__ == "__main__":
    main()
