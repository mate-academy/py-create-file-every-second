import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        filename = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        with open(filename, "w") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
