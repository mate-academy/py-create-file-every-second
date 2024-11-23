import time
from datetime import datetime


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = "app-" + time_now.strftime("%H_%M_%S") + ".log"
        with open(file_name, "w") as new_file:
            if int(time_now.strftime("%f")) == 0:
                timestamp = time_now.strftime("%Y-%m-%d %H:%M:%S")
            else:
                timestamp = time_now.strftime("%Y-%m-%d %H:%M:%S.%f")
            new_file.write(timestamp)
            print(timestamp + " " + file_name)
            new_file.close()
        time.sleep(1)


if __name__ == "__main__":
    main()
