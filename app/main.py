from datetime import datetime
import time


def main():
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w") as f:
            f.write(str(now))
            print(str(now) + f" app-{now.hour}_{now.minute}_{now.second}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
