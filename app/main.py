from datetime import datetime
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        with open(time_now.strftime("app-%H_%M_%S.log"), "w") as f:
            f.write(str(time_now))
            print(time_now, time_now.strftime("app-%H_%M_%S.log"))
            time.sleep(1)


if __name__ == "__main__":
    main()
