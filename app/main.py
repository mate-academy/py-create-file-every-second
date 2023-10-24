from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        hours = time_now.hour
        minutes = time_now.minute
        seconds = time_now.second
        name_log = f"app-{hours}_{minutes}_{seconds}.log"

        with open(name_log, "w") as f:
            f.write(str(time_now))
        print(str(time_now) + " " + name_log)
        time.sleep(1.0)


if __name__ == "__main__":
    main()
