from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now_time = datetime.now()
        timestamp = now_time.strftime("%Y-%m-%d %H:%M:%S")
        name = "app-" + now_time.strftime("%H_%M_%S") + ".log"
        with open(name, "w") as file:
            file.write(timestamp)
        print(f"{timestamp} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
