from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "a") as f:
            f.write(
                f"{now.year}-"
                f"{now.month}-"
                f"{now.day}"
                f" {now.hour}:"
                f"{now.minute}:"
                f"{now.second}"
            )
            print(f"{now.year:04d}-{now.month:02d}-{now.day:02d} "
                  f"{now.hour:02d}:{now.minute:02d}:{now.second:02d} "
                  f"app-{now.hour}_{now.minute}_{now.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
