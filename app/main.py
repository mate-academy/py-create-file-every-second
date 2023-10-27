import time
from datetime import datetime

while True:
    now = datetime.now()

    filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
    timestamp = str(now)

    with open(filename, "w") as f:
        f.write(timestamp)

    print(timestamp, filename)

    time.sleep(1)
