from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(timestamp)

        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
