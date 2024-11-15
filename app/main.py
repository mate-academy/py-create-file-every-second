import time
from datetime import datetime

stamp_time = datetime.fromtimestamp(1121545578)


def main() -> None:

    while True:
        time_now = datetime.now()
        time_file_name = (f"app-{time_now.hour}_"
                          f"{time_now.minute}_{time_now.second}.log")
        print(f"{time_now} {time_file_name}")
        with open(time_file_name, "w") as time_fail:
            time_fail.write(f"{time_now}")
        time.sleep(1)


if __name__ == "__main__":
    main()
