from datetime import datetime
from time import sleep


def main():
    while True:
        current_time = datetime.now()
        hours = f"{current_time.hour:02}"
        minutes = f"{current_time.minute:02}"
        seconds = current_time.second
        name_path = f"app-{hours}_{minutes}_{seconds}.log"

        with open(name_path, "w") as f:
            f.write(f"{current_time}")
            print(f"{current_time} {name_path}")

        sleep(1)


if __name__ == "__main__":
    main()
