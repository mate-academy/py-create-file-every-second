from datetime import datetime
import time


def main() -> None:

    while True:
        d1 = datetime.now()
        with open(f"app-{d1.hour}_{d1.minute}_{d1.second}.log", "w") as f:
            f.write(f"{datetime.now()}")
        time.sleep(1)


if __name__ == "__main__":
    main()
