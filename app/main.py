from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep

def main():


    while True:
        date_full = str(datetime.now()).split(".")[0]
        time_full = date_full.split(" ")[1]
        hours = time_full.split(":")[0]
        minutes = time_full.split(":")[1]
        seconds = time_full.split(":")[2]
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        content = date_full
        file_created = open(file_name, "w")
        file_created.write(f"{content}")
        print(f"{content} {file_name}")
        sleep(1)



if __name__ == "__main__":
    main()
