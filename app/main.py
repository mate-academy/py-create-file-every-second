from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second

        formatted_timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        with open(f"app-{hours}_{minutes}_{seconds}.log", "a") as f:
            f.write(formatted_timestamp)
        time.sleep(1)
        print(f"{formatted_timestamp} app-{hours}_{minutes}_{seconds}.log"
              )


if __name__ == "__main__":
    main()
