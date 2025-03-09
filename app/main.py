import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_now = datetime.now()
        time_name = time_now.strftime("%H_%M_%S")
        time_log = time_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"app-{time_name}.log", "w") as f:
            f.write(time_log)
        time.sleep(1)
        print(f"{time_log} app-{time_name}.log")


if __name__ == "__main__":
    main()
