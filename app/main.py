from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time = str(datetime.now())
        hours, minutes, seconds = time.split(" ")[1].split(":")
        seconds = int(seconds[0:2])
        name_file = f"app-{hours}_{minutes}_{seconds}.log"
        with open(name_file, "w") as file:
            file.write(time)
            print(f"{time} {name_file}")
        sleep(1)


if __name__ == "__main__":
    main()
