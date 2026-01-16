from datetime import datetime
import time             # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        now_time = now.strftime("%H_%M_%S")
        name_file = f"app-{now_time}.log"
        with open(name_file, "a") as file:
            timestamp = str(now)
            file.write(f"{timestamp}")
            print(f"{timestamp} {name_file}")
        time.sleep(1)


if __name__ == "__main__":
    main()
