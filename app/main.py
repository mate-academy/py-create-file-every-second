import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w") as f:
            f.write(timestamp_str)
        print(f"{timestamp_str} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
