from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()

        filename = now.strftime("app-%H_%M_%S.log")

        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(timestamp_str)

        print(f"{timestamp_str} {filename}")

        time.sleep(1)


if __name__ == "__main__":
    main()
