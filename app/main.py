from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        today = datetime.now()
        with open(f"{today.strftime('app-%H_%M_%S.log')}", "w") as f:
            f.write(f"{today}")
        print(f"{today} {today.strftime('app-%H_%M_%S.log')}")
        time.sleep(1)
    pass


if __name__ == "__main__":
    main()
