from datetime import datetime
from time import sleep


def main() -> str:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, mode="w") as f:
            f.write(str(now))
        print(f"{now} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
