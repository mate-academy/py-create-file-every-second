from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_date = str(datetime.now().replace(microsecond=0))
        hours = current_date[11:13]
        minutes = current_date[14:16]
        seconds = current_date[17:]
        if len(seconds) == 2 and "0" in seconds[0]:
            seconds.replace("0", "")
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(current_date)
        print(current_date, f"app-{hours}_{minutes}_{seconds}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
