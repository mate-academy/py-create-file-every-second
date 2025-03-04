import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:

        date_time_now = datetime.now()
        hours = date_time_now.strftime("%H")
        minutes = date_time_now.strftime("%M")
        seconds = date_time_now.strftime("%S")
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as file:
            time_now = date_time_now.strftime("%Y-%m-%d %H:%M:%S")
            file.write(time_now)

            print(f"{time_now} {filename}")
            time.sleep(1)


if __name__ == "__main__":
    main()
