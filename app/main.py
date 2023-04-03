from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            line = str(now)
            f.write(line)
        with open(f"app-{hours}_{minutes}_{seconds}.log", "r") as f:
            print(f.read() + " " + f"app-{hours}_{minutes}_{seconds}.log")
        sleep(1)


if __name__ == "__main__":
    main()
