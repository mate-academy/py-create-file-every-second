from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()

        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        timestamp = str(now)

        with open(file_name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
