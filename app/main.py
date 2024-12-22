from datetime import datetime
from time import sleep
import os

def create_file():
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, 'w') as f:
            f.write(timestamp)
        print(f"{timestamp} {file_name}")
        sleep(1)

if __name__ == "__main__":
    create_file()
