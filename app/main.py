import datetime
import time

while True:

    date_now = datetime.datetime.now()
    full_date = f"app-{date_now.hour}_{date_now.minute}_{date_now.second}.log"

    with open(full_date, 'w') as file:
        file.write(str(date_now))

    print(str(date_now) + ' ' + full_date)
    time.sleep(1)
