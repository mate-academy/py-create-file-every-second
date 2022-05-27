import os
from datetime import datetime
import time


while True:
    file_content = datetime.now()
    hour = file_content.hour
    minute = file_content.minute
    second = file_content.second
    file_name = f"{os.path.basename(os.getcwd())}" \
                f"-{hour}" \
                f"_{minute}" \
                f"_{second}.log"
    with open(file_name, "w", encoding="utf8") as log_file:
        log_file.write(f"{file_content}\n")
        print(f"{file_content}"
              f" {os.path.basename(os.getcwd())}"
              f"-{hour}"
              f"_{minute}"
              f"_{second}.log")
        time.sleep(1)
