from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        ts_long = str(datetime.now())
        ts = ts_long[:ts_long.index(".")]
        hrs = ts[ts.index(" ") + 1:ts.index(":")]
        mins = ts[ts.index(":") + 1:ts.rindex(":")]
        secs = ts[ts.rindex(":") + 1:]
        log_name = f"app-{hrs}_{mins}_{secs}.log"
        log = open(log_name, "w")
        print(ts, log_name)
        log.write(ts)
        log.close()
        sleep(1)


if __name__ == "__main__":
    main()
