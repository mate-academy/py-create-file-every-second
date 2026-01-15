from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = str(datetime.now())
        hours = time_now[11:13]
        minutes = time_now[14:16]
        seconds = time_now[17:19]
        f_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(f_name, "w") as f:
            f.write(time_now)
        print(time_now, f_name)
        sleep(1)


if __name__ == "__main__":
    main()
