from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w") as f:
            f.write(timestamp)
        print(f"{timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
