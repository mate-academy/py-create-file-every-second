import os
from datetime import datetime
import time


while True:
    file_content = datetime.now()
    file_name = f"{os.path.basename(os.getcwd())}" \
                f"-{file_content.hour}" \
                f"_{file_content.minute}" \
                f"_{file_content.second}.log"
    with open(file_name, "w", encoding="utf8") as log_file:
        log_file.write(f"{file_content}\n")
        print(f"{file_content}"
              f" {os.path.basename(os.getcwd())}"
              f"-{file_content.hour}"
              f"_{file_content.minute}"
              f"_{file_content.second}.log")
        time.sleep(1)
