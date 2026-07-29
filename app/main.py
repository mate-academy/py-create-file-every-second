from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        hour_now = datetime.now().strftime('%H')
        minute_now = datetime.now().strftime('%M')
        second_now = datetime.now().strftime('%S')
        with open(f"app-{hour_now}_{minute_now}_{second_now}.log", "w") as f:
            f.write(f"{datetime.now()}")
            print(f"{datetime.now()} "
                  f"app-{hour_now}_{minute_now}_{second_now}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
