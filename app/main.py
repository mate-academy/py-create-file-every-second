from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


while True:
    now = datetime.now()
    file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "w") as f:
        f.write(timestamp)

    print(timestamp, file_name)
    sleep(1)
