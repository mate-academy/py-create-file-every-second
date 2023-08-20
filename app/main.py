from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        time = str(datetime.now())
        name_log = f"app-{time[11:13]}_{time[14:16]}_{time[17:19]}.log"

        with open(name_log, "w") as f:
            f.write(time)
            print(time, f"app-{time[11:13]}_{time[14:16]}_{time[17:19]}.log")
            sleep(1)


if __name__ == "__main__":
    main()
