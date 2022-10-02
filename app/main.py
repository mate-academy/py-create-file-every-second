from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    full_time_now = datetime.now()
    time_split = str(full_time_now).split()
    only_time_now = time_split[1]
    hours_split = only_time_now.split(":")

    hours = hours_split[0]
    minutes = hours_split[1]

    seconds_with_milliseconds = hours_split[2]
    seconds_split = seconds_with_milliseconds.split(".")
    seconds = seconds_split[0]

    while True:
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(str(file_name))
        with open(file_name, "r") as f:
            print(f.read())
        time.sleep(1)


if __name__ == "__main__":
    main()
