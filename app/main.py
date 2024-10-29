from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep

def main():
    while True:
        datetime_now = datetime.now()	
        hours = datetime_now.hour
        minutes = datetime_now.minute
        seconds = datetime_now.second
        if datetime_now.microsecond == 0:
            timestamp_str = datetime_now.strftime("%Y-%m-%d %H:%M:%S")
        if datetime_now.microsecond != 0:
            timestamp_str = datetime_now.strftime("%Y-%m-%d %H:%M:%S.%f")
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as f:
             f.write(timestamp_str)
        print(f"{timestamp_str} {filename}")            
        sleep(1)


if __name__ == "__main__":
    main()
