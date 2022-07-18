import time
from datetime import datetime


def main():
    while True:
        t = datetime.now()
        name = f"app-{t.hour}_{t.minute}_{t.second}.log"
        with open(name, "w") as f:
            f.write(str(datetime.now()))
        print(t, name)
        time.sleep(1)


if __name__ == "__main__":
    main()
