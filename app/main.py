from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> str:
    while True:
        with open(f"app-{datetime.now().strftime('%H_%M_%S')}.log", "w") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
              f"app-{datetime.now().strftime("%H_%M_%S")}.log")
        time.sleep(1)
    # write your code here
    pass


if __name__ == "__main__":
    main()
