from datetime import datetime
import time


def main():
    while True:
        now = datetime.now()
        current_time = now.strftime("app-%H_%M_%S.log")
        with open(current_time, "a") as f:
            f.write(str(now))
        print(f"{now} {current_time}")
        time.sleep(1)


if __name__ == "__main__":
    main()
