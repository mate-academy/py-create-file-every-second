from datetime import datetime
import time


while True:
    now = datetime.now()
    file_name = f"app-{now.strftime('%H_%M_%S')}.log"
    with open(f"{file_name}.txt", "w") as file:
        file.write(str(now))
    print(f"{now} {file_name}")
    time.sleep(1)
