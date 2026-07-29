from datetime import datetime
import time


def main() -> None:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{datetime.now().strftime('%H_%M_%S')}.log"

        with open(file_name, "w") as f:
            f.write(timestamp)
        print(f"{timestamp} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
