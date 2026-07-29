from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"

        with open(filename, "w") as f:
            f.write(timestamp_str)

        print(f"{timestamp_str} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
