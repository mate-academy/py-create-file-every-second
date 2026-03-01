from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.strftime('%H_%M_%S')}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(timestamp)

        print(timestamp, filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
