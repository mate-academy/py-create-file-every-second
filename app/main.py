from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        now1 = f"app-{now.strftime('%H_%M_%S')}.log"
        with open(now1, "w") as file:
            file.write(str(datetime.now()))
            print(f"{now} {now1}")
            time.sleep(1)


if __name__ == "__main__":
    main()
