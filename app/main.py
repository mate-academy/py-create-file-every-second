import datetime
import time


def main():
    while True:
        current_time = datetime.datetime.now()
        time_for_name = current_time.time().isoformat(timespec="seconds")
        name_of_file = f'app-{time_for_name.replace(":", "_")}.log'
        current_time_iso = current_time.isoformat(sep=" ")

        with open(name_of_file, "w") as f:
            f.write(current_time_iso)
            print(current_time_iso, name_of_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
