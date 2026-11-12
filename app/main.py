from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        with open(f"app-{datetime.now().hour}_{datetime.now().minute}"
                  f"_{datetime.now().second}.log", "w") as f:
            f.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} "
              f"app-{datetime.now().hour}_{datetime.now().minute}"
              f"_{datetime.now().second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
