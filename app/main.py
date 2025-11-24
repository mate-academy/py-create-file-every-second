from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours, minutes, seconds = now.hour, now.minute, now.second
        name = f"app-{hours}_{minutes}_{seconds}.log"
        print(now.strftime("%Y-%m-%d %H:%M:%S"), name)
        with open(name, "w") as f:
            #2020-01-01 14:10:07
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        sleep(1)


if __name__ == "__main__":
    main()
