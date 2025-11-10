from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        ts = now.strftime("%Y-%m-%d %H:%M:%S")
        name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(name, "w") as f:
            f.write(ts)
        print(ts, name)
        sleep(1)


if __name__ == "__main__":
    main()
