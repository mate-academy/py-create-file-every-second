from datetime import datetime
import time


def main() -> None:
    while True:
        with open(f"app-{datetime.now().hour}_{datetime.now().minute}_"
                  f"{datetime.now().second}.log", "w") as file:
            file.write(f"{datetime.now()}")
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} app-"
                  f"{datetime.now().hour}_{datetime.now().minute}_"
                  f"{datetime.now().second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
