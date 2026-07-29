from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now().replace(microsecond=0)
        time_log = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(time_log, "w") as file:
            file.write(str(time))
        print(time, time_log)
        sleep(1)


if __name__ == "__main__":
    main()
