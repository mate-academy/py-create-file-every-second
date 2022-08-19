from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    now = datetime.now()
    current_time = f"{now.hour}_{now.minute}_{now.second}"
    while True:
        with open(f"app-{current_time}.log", "w") as f:
            f.write(f"{now}")
            print(now, f"app-{current_time}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
