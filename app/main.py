from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = str(datetime.now())
        name = \
            f"app-{int(time[11:13])}_{int(time[14:16])}_{int(time[17:19])}.log"
        with open(name, "w") as f:
            print(f"{time} {name}")
            f.write(time)
        sleep(1)


if __name__ == "__main__":
    main()
