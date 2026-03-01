from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        data_now = str(datetime.now()).split(".")[0]
        now = datetime.now()
        hours, mins, sec = now.hour, now.minute, now.second
        with open(f"app-{hours}_{mins}_{sec}.log", "w") as f:
            f.write(f"{data_now}")
            print(f"{data_now} app-{hours}_{mins}_{sec}.log")
        sleep(1)


if __name__ == "__main__":
    main()
