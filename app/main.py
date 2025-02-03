from datetime import datetime
from time import sleep

while True:
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")

    filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

    with open(filename, "w") as file:
        file.write(timestamp)

    print(timestamp, filename)

    sleep(1)
