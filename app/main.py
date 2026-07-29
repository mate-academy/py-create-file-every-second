from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        time_str = time_now.strftime("%H_%M_%S")
        with open(f"app-{time_str}.log", "w") as f:
            time.sleep(1)
            f.write(str(time_now))
            print(time_now, f"app-{time_str}.log")


if __name__ == "__main__":
    main()
