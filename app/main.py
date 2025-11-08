from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.strftime("%H_%M_%S")}.log"
        sleep(1)
        with open(file_name, "w") as w:
            w.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
        with open(file_name, "r") as r:
            print(r.readline(), file_name)


if __name__ == "__main__":
    main()
