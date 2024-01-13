from datetime import datetime  # DO NOT CHANGE THIS IMPOR
import time
import os
import sys


def main():
    os.chdir(os.path.dirname(sys.argv[0]))
    while True:
        current_datetime = datetime.now()
        file_name = f"app-{datetime.now().hour}_{datetime.now().minute}_{datetime.now().second}.log"
        new_file = open(file_name, "w")
        new_file.write(str(datetime.now()))
        new_file.close()
        print(f"{datetime.now()} {file_name}")
        time.sleep(1)
        
if __name__ == "__main__":
    main()
