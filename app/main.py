import time
from datetime import datetime


def main() -> None:
    while True:
        moment = datetime.now()
        filename = (f"app-{moment.strftime('%H')}_"
                    f"{moment.strftime('%M')}_"
                    f"{moment.strftime('%S')}.log")
        with open(filename, "w") as f:
            f.write(f"{moment.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{moment.strftime('%Y-%m-%d %H:%M:%S')} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
