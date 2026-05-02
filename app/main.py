from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        timee = datetime.now()
        seconds = timee.second
        minutes = timee.minute
        hours = timee.hour
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as f:
            now = timee.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{now} {filename}", flush=True)
            f.write(now)
        sleep(1)


if __name__ == "__main__":
    main()
