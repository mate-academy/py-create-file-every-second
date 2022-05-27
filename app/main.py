from datetime import datetime
import time


while True:
    time.sleep(1)
    current_time = datetime.now()
    time_for_name = current_time.time().isoformat(timespec="seconds")
    name_of_file = f'app-{time_for_name.replace(":", "_")}.log'
    current_time_iso = current_time.isoformat(sep=" ")

    with open(name_of_file, "w") as f:
        f.write(current_time_iso)
        print(current_time_iso, name_of_file)
