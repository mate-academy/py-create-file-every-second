from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_t = datetime.now().strftime("%H_%M_%S")
        title = f"app-{time_t}.log"
        timestamp = f"{datetime.now()}"
        with open(title, "a") as f:
            f.write(f"{timestamp}")
            print(f"{timestamp} {title}")
            sleep(1)


if __name__ == "__main__":
    main()
