from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        now_time_file = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        with open(now_time_file, "w") as f:
            f.write(now_time)

        with open(now_time_file, "r") as f:
            print(f.read() + " " + now_time_file)

        sleep(1)


if __name__ == "__main__":
    main()
