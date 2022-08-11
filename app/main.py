from datetime import datetime
import time


def main():
    while True:
        name = f"app-{datetime.now().hour}" \
               f"_{datetime.now().minute}" \
               f"_{datetime.now().second}.log"
        timestamp = datetime.now()
        with open(name, "w") as f:
            f.write(f"{timestamp}")
            print(timestamp, name)
            time.sleep(1)


if __name__ == "__main__":
    main()
