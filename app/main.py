from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(name, "w") as file_time:
            file_time.write(str(now))
        print(f"{str(now)[:19]} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
