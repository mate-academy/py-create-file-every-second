from datetime import datetime
import time


def main() -> None:

    while True:

        data_time = datetime.now()

        hour = data_time.hour
        minute = data_time.minute
        second = data_time.second
        date_now = data_time.date()
        clock = data_time.time().replace(microsecond=0)

        with open(f"app-{hour}_{minute}_{second}.log", "w") as f:
            f.write(f"{date_now} {clock}")
            print(f"{date_now} {clock} {f.name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
