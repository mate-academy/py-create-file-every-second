from datetime import datetime
import time


while True:
    file_name = "app-" + datetime.now().strftime("%H_%M_%S") + ".log"
    content = str(datetime.now())
    with open(file_name, "x") as file:
        file.write(content)
    time.sleep(1)
