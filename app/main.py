from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hours = datetime.now().strftime("%H")
        minutes = datetime.now().strftime("%M")
        seconds = datetime.now().strftime("%S")
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(time)
            print(time + f" app-{hours}_{minutes}_"
                         f"{'0' if seconds == '00' else seconds}.log")
            sleep(1)


if __name__ == "__main__":
    main()
