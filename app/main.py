from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w") as f:
            f.write(timestamp)

        print(timestamp, filename)

        time.sleep(1)


if __name__ == "__main__":
    main()
