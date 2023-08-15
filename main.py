from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_stamp = datetime.now()
        file_name = (f"app-{time_stamp.hour}_"
                     f"{time_stamp.minute}_{time_stamp.second}.log")
        with open(file_name, "x") as f:
            f.write(str(time_stamp))
            print(time_stamp, file_name)
        sleep(1)


if __name__ == "__main__":
