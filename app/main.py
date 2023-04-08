from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = str(datetime.now())
        day_time = time_now.split(" ")
        day_time = day_time[1]
        name_file = day_time.split(".")
        name_file = name_file[0]
        name_file = name_file.replace(":", "_")
        with open(f"app-{name_file}.log", "w") as time_file:
            time_file.write(time_now)
            print(time_now, f"app-{name_file}.log")
            sleep(1.0)


if __name__ == "__main__":
    main()
