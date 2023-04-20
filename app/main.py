from datetime import datetime
import time


def main():
    while True:
        current_time = datetime.now().strftime("%H_%M_%S")
        with open(f"app-{current_time}.log", "w") as f:
            f.write(f"{datetime.now()}")
            print(f"{datetime.now()} app-{current_time}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
