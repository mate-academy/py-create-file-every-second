from datetime import datetime
from time import sleep


while True:
    current_time = datetime.now()

    file_name = current_time.strftime("app-%H_%M_%S.log")
    with open(file_name, "w") as log_file:
        log_file.write(str(current_time))

    print(current_time, file_name)
    sleep(1)
