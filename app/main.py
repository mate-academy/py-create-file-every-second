from datetime import datetime
from time import sleep


def main():
    while True:
        str_time = datetime.now().__str__()
        hours = str_time[11:13]
        minutes = str_time[14:16]
        seconds = str_time[17:19]
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(str_time)
            print(str_time + " " + f.name)
            sleep(1)


if __name__ == "__main__":
    main()
