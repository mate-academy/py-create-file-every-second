from datetime import datetime

start = datetime.now().second

while True:
    now = datetime.now()
    while start == now.second:
        now = datetime.now()

    start = now.second

    try:
        file = open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w")
        file.write(str(now))
    except IOError as e:
        print(e)
    else:
        print(now, file.name)
        file.close()
