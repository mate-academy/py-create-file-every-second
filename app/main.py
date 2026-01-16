from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        title = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(title, "w") as f:
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            f.write(timestamp)

        print(f"{timestamp} {title}")
        time.sleep(1)


if __name__ == "__main__":
    main()
