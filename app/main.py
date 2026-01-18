import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_datetime = str(datetime.now())
        current_time = current_datetime.split()[1].split(".")[0].split(":")
        hours = current_time[0]
        minutes = current_time[1]
        seconds = current_time[2]
        name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(name, "w") as file:
            file.write(current_datetime)
        print(str(datetime.now()), name)
        time.sleep(1)


if __name__ == "__main__":
    main()
