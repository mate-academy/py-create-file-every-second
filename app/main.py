import time
from datetime import datetime

while True:
    now = datetime.now()
    file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

    with open(file_name, "w") as f:
        f.write(now.isoformat())

    print(f"{now} {file_name}")

    time.sleep(1)