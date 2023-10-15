from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = f"{current_time.strftime('app-%H_%M_%S.log')}"
        with open(filename, "w") as f:
            f.write(f"{datetime.now()}")
            print(f"{datetime.now()} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
