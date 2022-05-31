from datetime import datetime
from time import sleep


while True:
    date_now = datetime.now()
    time_info = f"{datetime.now().hour}_" \
                f"{datetime.now().minute}_" \
                f"{datetime.now().second}"
    with open(f"{time_info}.log", "w") as log_file:
        log_file.write(f"{date_now}")
        print(f"file with name {time_info}.log "
              f"was created {date_now}")
        sleep(1)
