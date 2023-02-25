from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        filename = f"app-{datetime.now().hour}_" \
                   f"{datetime.now().minute}_" \
                   f"{datetime.now().second}.log"
        timestamp = str(datetime.now())
        with open(filename, "w") as f:
            f.write(timestamp)
            print(f"{timestamp} {filename}")
            sleep(1)


if __name__ == "__main__":
    main()
