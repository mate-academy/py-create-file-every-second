from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(str(now))
            print(str(now), file.name)
        sleep(1)


if __name__ == "__main__":
    main()
