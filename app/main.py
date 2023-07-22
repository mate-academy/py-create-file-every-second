import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        work_time = datetime.now()
        work_file = ("app-{}_{}_{}.log".format(
            work_time.hour,
            work_time.minute,
            work_time.second
        ))
        with open(work_file, "w") as file_log:
            file_log.write(str(work_time))
        print(str(work_time) + " " + work_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
