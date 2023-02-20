from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        with open(f"app-{time_now.strftime('%H_%M_%S')}.log", "w") as file:
            file.write(str(time_now))
            print(time_now, f"app-{time_now.strftime('%H_%M_%S')}.log")
            sleep(1)


if __name__ == "__main__":
    main()
