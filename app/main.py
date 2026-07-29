from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        now2 = datetime.now().strftime("%H_%M_%S")
        with open(f"app-{now2}.log", "w") as f:
            f.write(now)
        print(f"{now} app-{now2}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
