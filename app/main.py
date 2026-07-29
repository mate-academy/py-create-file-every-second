from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        time_str = time.strftime("%H_%M_%S")
        with open(f"app-{time_str}.log", "w") as f:
            sleep(1)
            f.write(str(time))
            print(time, f"app-{time_str}.log")


if __name__ == "__main__":
    main()
