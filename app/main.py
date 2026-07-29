import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date_time = str(datetime.now())
        with open(f"app-{date_time[11:13]}_"
                  f"{date_time[14:16]}_"
                  f"{date_time[17:]}.log", "w") as f:
            f.write(f"{date_time}")
            print(date_time
                  + f" app-{date_time[11:13]}_"
                  f"{date_time[14:16]}_"
                  f"{date_time[17:]}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
