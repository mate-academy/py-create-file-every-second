import datetime
import time


def create_file_every_second():
    while True:
        dt = datetime.datetime.now()
        hours = dt.time().hour
        minutes = dt.time().minute
        seconds = dt.time().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        file_line = dt.isoformat(sep=" ")
        with open(file_name, "w") as f:
            f.write(file_line)
        print(file_line, file_name)
        time.sleep(1)


if __name__ == "__main__":
    create_file_every_second()
