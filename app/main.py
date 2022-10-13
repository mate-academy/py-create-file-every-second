from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        times = datetime.now()
        seconds = times.second
        minutes = times.minute
        hours = times.hour
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "a") as f:
            f.write(f"{times}")
            print(times, file_name)
            time.sleep(1)


if __name__ == "__main__":
    main()
