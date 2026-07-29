from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = str(datetime.now())
        hrs, mins, secs = now.split()[1].split(":")
        secs = secs[:2]
        fname = f"app-{hrs}_{mins}_{secs}.log"
        with open(fname, "w") as f:
            f.write(now)
        print(now, fname)
        sleep(1)


if __name__ == "__main__":
    main()
