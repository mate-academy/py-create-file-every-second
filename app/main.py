from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second

        filename = f"app-{hours}_{minutes}_{seconds}.log"

        with open(filename, "w") as f:
            now = str(datetime.now())
            f.write(now)
            print(f"{now} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
