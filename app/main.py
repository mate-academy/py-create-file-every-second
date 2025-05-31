from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date_now = str(datetime.now()).split()[-1].split(".")[0]
        hours = date_now.split(":")[0]
        minutes = date_now.split(":")[1]
        seconds = date_now.split(":")[2]

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(f"2025-05-31 {hours}:{minutes}:{seconds}")
        print(str(datetime.now()).split(".")[0], f"app-{hours}_{minutes}_{seconds}.log")
        sleep(1)


if __name__ == "__main__":
    main()
