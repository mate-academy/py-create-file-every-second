from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        current_time = now.time()
        time_str = str(current_time).split(".")[0].replace(":", "_")
        timestamp = str(now).split(".")[0]

        with open(f"app-{time_str}.log", "w") as f:
            f.write(timestamp)

        print(timestamp, f"app-{time_str}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
