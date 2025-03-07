import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{now.strftime("%H_%M_%S")}.log"

        with open(filename, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
