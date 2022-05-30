import os
from datetime import datetime
import time


def create_file_every_second():
    while True:

        file_content = datetime.now()

        hour = file_content.hour
        minute = file_content.minute
        second = file_content.second

        last_part_file_name = f"-{hour}_{minute}_{second}.log"
        file_name = f"{os.path.basename(os.getcwd())}{last_part_file_name}"

        with open(file_name, "w", encoding="utf8") as log_file:
            log_file.write(f"{file_content}\n")
            print(f"{file_content}"
                  f" {os.path.basename(os.getcwd())}"
                  f"{last_part_file_name}")
            time.sleep(1)
