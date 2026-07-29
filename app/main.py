import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()

        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            print(current_time, f.name)
            f.write(str(current_time))

        time.sleep(1)


if __name__ == "__main__":
    main()
