import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now_time = datetime.now()
        hours = now_time.hour
        minutes = now_time.minute
        seconds = now_time.second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(str(now_time))
            print(str(now_time) + f" app-{hours}_{minutes}_{seconds}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
