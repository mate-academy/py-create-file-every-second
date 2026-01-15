from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        now_str = str(now)
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(now_str)
            time.sleep(1)
            print(now_str, f.name)


if __name__ == "__main__":
    main()
