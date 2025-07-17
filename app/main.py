import time
from datetime import datetime

def main() -> None:
    while True:
        date_now = datetime.now().strftime("%Y-%m-%d")
        time_now = datetime.now().strftime("%H:%M:%S")
        filename = f"app-{time_now.replace(':', '_')}.log"

        with open(filename, "w") as f:
            f.write(f"{date_now} {time_now}")
        print(f"{date_now} {time_now} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
