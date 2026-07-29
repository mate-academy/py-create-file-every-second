from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_and_time = datetime.now()
        hours = date_and_time.hour
        minutes = date_and_time.minute
        seconds = date_and_time.second
        formatted = date_and_time.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as f:
            f.write(f"{formatted}")
        print(f"{formatted} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
