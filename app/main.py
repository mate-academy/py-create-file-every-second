from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        now_file = open(f"app-{date.hour}_{date.minute}_{date.second}"
                        + ".log", "w")
        now_file.write(str(date))
        print(date, f"app-{date.hour}_{date.minute}_{date.second}" + ".log")
        now_file.close()
        sleep(1)


if __name__ == "__main__":
    main()
