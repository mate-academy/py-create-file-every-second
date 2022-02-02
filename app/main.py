import datetime
import time

while True:

    date_now = str(datetime.datetime.now())
    full_date = f"app-{date_now.split(' ')[1][:8].replace(':', '_')}.log"

    with open(full_date, 'w') as file:
        file.write(date_now)

    print(date_now + ' ' + full_date)
    time.sleep(1)
