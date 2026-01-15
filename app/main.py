from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hours = time_now[11:13]
        minutes = time_now[14:16]
        seconds = time_now[17:19]
        new_file = f"app-{hours}_{minutes}_{seconds}.log"
        with open(new_file, "w") as file:
            file.write(time_now)
        print(f"{time_now} {new_file}")
        sleep(1)


if __name__ == "__main__":
    main()
