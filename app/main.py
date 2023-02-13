from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        time.sleep(1)
        with open(f"app-{now.strftime('%H_%M_%S')}.log", "w") as f:
            f.write(str(now))
        name = open(f"app-{now.strftime('%H_%M_%S')}.log", "r")
        print(name.read() + f" app-{now.strftime('%H_%M_%S')}.log")
        name.close()


if __name__ == "__main__":
    main()
