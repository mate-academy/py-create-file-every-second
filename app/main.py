from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        hrs, mins, secs = now.split()[1].split(":")
        secs = secs if secs[0] != "0" else secs[1]
        with open(f"app-{hrs}_{mins}_{secs}.log", "w") as f:
            f.write(now)
        sleep(1)


if __name__ == "__main__":
    main()
