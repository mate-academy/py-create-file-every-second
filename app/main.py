from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        name = f"app-{hours:02d}_{minutes:02d}_{seconds:02d}.log"
        with open(name, "w") as file:
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp)
        print(timestamp, name)
        sleep(1)


if __name__ == "__main__":
    main()
