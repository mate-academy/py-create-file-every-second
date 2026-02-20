from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:

    while True:
        now = datetime.now()
        now_hour = now.hour
        now_minute = now.minute
        now_sec = now.second
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{now_hour}_{now_minute}_{now_sec}.log"
        with open(filename, "w") as file:
            file.write(timestamp)
        print(timestamp , filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
