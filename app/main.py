import time
from datetime import datetime


def main() -> None:
    now = datetime.now()
    while True:
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(timestamp)
            print(f"{timestamp} {file_name}")
        time.sleep(1)

if __name__ == "__main__":
    main()
