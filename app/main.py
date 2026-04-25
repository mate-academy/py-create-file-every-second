from datetime import datetime
import time


def main() -> None:

    while True:
        now_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        now_time = datetime.now().strftime("%H_%M_%S")
        with open(f"app-{now_time}.log", "w") as f:
            time.sleep(1)
            f.write(now_date)
            print(now_date, f"app-{now_time}.log")


if __name__ == "__main__":
    main()
