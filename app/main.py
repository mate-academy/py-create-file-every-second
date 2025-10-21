from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = f"{now.date()} {now.hour:02d}:{now.minute:02d}:{now.second:02d}"
        filename = f"app-{now.hour:02d}_{now.minute:02d}_{now.second:02d}.log"

        print(f"{timestamp} {filename}")

        with open(filename, "w") as f:
            f.write(timestamp)

        sleep(1)


if __name__ == "__main__":
    main()
