from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        dt = datetime.now()
        time_stamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        hour = dt.hour
        minute = dt.minute
        second = dt.second
        file_name = f"app-{hour}_{minute}_{second}.log"
        with open(file_name, "w") as file:
            file.write(time_stamp)
        print(time_stamp, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
