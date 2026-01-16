from datetime import datetime
import time


def main():
    while True:
        today = datetime.now()
        name = f"app-{today.hour}_{today.minute}_{today.second}.log"
        f = open(name, "w")
        f.write(str(today))
        print(f"{datetime.now()} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
