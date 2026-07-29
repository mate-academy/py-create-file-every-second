from time import sleep
from datetime import datetime


def main() -> None:
    while True:
        time_now = datetime.now().replace(microsecond=0)
        filename = (f"app-{time_now.hour}_{time_now.minute}_{time_now.second}"
                    f".log")
        with open(filename, "x") as f:
            f.write(str(time_now))
            print(f"{time_now} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
