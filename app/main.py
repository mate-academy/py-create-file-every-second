from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = str(datetime.now())
        time = date.split()[1].split(":")
        hour = time[0]
        minute = time[1]
        second = int(time[2])
        fl = f"app-{hour}_{minute}_{second}.log"
        with open(fl, "w") as fn:
            fn.write(date)
        print(date, fl)
        sleep(1)


if __name__ == "__main__":
    main()
