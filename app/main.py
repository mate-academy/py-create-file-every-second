from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w") as f:
            f.write(now.strftime('%Y-%m-%d %H:%M:%S'))
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
