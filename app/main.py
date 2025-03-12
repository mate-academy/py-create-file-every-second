import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        act = datetime.now()
        name = f"app-{act.hour}_{act.minute}_{act.second}.log"
        with open(name, "w+") as fil:
            fil.write(act.strftime("%Y-%m-%d %H:%M:%S"))
            fil.seek(0)
            print(fil.read(), fil.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
