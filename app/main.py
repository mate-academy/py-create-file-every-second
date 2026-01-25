from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        correct_date = str(datetime.now()).strip().split("-")
        correct_time = correct_date[-1].split()
        final_time = correct_time[-1].split(":")

        hour = final_time[0]
        minute = final_time[1]
        second = final_time[-1].split(".")[0]

        current_name = f"app-{hour}_{minute}_{second}.log"
        timestamp = str(datetime.now()).split(".")[0]

        with open(current_name, "w") as f:
            f.write(timestamp)

        print(timestamp, current_name)
        sleep(1)


if __name__ == "__main__":
    main()
