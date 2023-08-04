import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = "app-" + current_time.strftime("%H_%M_%S") + ".log"
        with open(file_name, "a") as f:
            f.write(str(current_time))
            time.sleep(1)
            print(current_time, file_name)


if __name__ == "__main__":
    main()
