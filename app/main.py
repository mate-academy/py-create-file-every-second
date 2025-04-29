import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            timestamp = str(datetime.now()).split(".")[0]
            f.write(timestamp)
            print(timestamp, f.name)
            time.sleep(1)


if __name__ == "__main__":
    main()
