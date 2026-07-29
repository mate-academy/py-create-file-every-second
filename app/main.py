from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        with open(f"app-{current_time.strftime('%H_%M_%S')}.log", "w") as f:
            f.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))

        print(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} "
              f"app-{current_time.strftime('%H_%M_%S')}.log")

        time.sleep(1)


if __name__ == "__main__":
    main()
