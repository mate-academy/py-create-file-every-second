from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        with open(
            f"app-{hours}_{minutes}_{seconds}.log",
            "w"
        ) as day_f:
            day_f.write(str(now))
        print(now, f"app-{hours}_{minutes}_{seconds}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
