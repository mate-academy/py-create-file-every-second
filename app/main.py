from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        with open(f"app-{datetime.now().hour}_"
                  f"{datetime.now().minute}_"
                  f"{datetime.now().second}.log", "w") as log:
            now = datetime.now()
            log.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " " + log.name)
        sleep(1)


if __name__ == "__main__":
    main()
