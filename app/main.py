from datetime import datetime
from time import sleep


while True:
    now = datetime.now()
    now_file_name = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
    with open(now_file_name, "w") as f:
        f.write(str(now))
        print(now_file_name)
        print(str(now))
        sleep(1)
