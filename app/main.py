from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        date_now = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(date_now, "w") as new_date_now:
            new_date_now.write(str(now))
        print(f"{now} {date_now}")
        sleep(1)


if __name__ == "__main__":
    main()
