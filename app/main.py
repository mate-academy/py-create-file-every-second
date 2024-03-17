import time
from datetime import datetime


def main() -> None:
    while 1:
        time_now = datetime.now()
        name = f"app-{time_now.hour}_{time_now.minute}_{time_now.second}.log"
        with open(name, "w") as f:
            f.write(str(time_now))
        print(time_now, name)
        time.sleep(1)


if __name__ == "__main__":
    main()
