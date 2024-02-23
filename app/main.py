from datetime import datetime
from time import sleep


def main() -> None:

    while True:
        current_time = datetime.now()

        time_stamp = str(current_time).split()[1]
        split_time_stamp = time_stamp.split(":")

        hours = split_time_stamp[0]
        minutes = split_time_stamp[1]
        seconds = split_time_stamp[2].split(".")[0]

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(str(current_time))

        print(f"{current_time} {f.name}")

        sleep(1)


if __name__ == "__main__":
    main()
