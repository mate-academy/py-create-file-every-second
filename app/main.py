from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        ts = str(datetime.now())
        hrs = ts[ts.index(" ") + 1:ts.index(":")]
        mins = ts[ts.index(":") + 1:ts.rindex(":")]
        secs = ts[ts.rindex(":") + 1:]
        log = open(f"{ts} app-{hrs}_{mins}_{secs}.log", "w")
        log.write(ts)
        log.close()
        sleep(1)


if __name__ == "__main__":
    main()
