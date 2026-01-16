from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = str(datetime.now())
        curr_time = f"app-{date[11:13]}_{date[14:16]}_{date[17:19]}.log"
        with open(curr_time, "w") as f:
            f.write(f"{date[:19]}")
        print(date[:19] + " " + curr_time)
        sleep(1)


if __name__ == "__main__":
    main()
