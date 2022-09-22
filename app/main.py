from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        timestamp = datetime.now()
        filename = timestamp.strftime("app-%H_%M_%S.log")

        with open(filename, "w") as f:
            f.write(f"{timestamp}")

        print(timestamp, filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
