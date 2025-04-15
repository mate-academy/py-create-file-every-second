import time
from datetime import datetime

def create_log_file():
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w") as f:
            f.write(timestamp)
        print(f"{timestamp} {filename}")
        time.sleep(1)

if __name__ == "__main__":
    create_log_file()