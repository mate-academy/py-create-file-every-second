from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = str(datetime.now())
        hours = time_now[11:13]
        minutes = time_now[14:16]
        seconds = time_now[17:19]

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(f"{time_now}")
            print(f"{time_now} app-{hours}_{minutes}_{seconds}.log")

        sleep(1)


if __name__ == "__main__":
    main()
