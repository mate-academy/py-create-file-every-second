from datetime import datetime
from time import sleep


def main():
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        sleep(1)
        with open(filename, "w") as log:
            log.write(timestamp)
            print(f"{timestamp} {filename}")


if __name__ == "__main__":
    main()
