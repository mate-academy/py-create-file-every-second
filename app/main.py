from datetime import datetime
from time import sleep

while True:
    now = datetime.now()
    file_name = now.strftime("app-%H_%M_%S.log")

    with open(f"{file_name}", "w") as file:
        file.write(f"{now}")

    print(f"{now} {file_name}")
    sleep(1)
