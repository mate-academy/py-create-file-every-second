from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep

def main():
    while True:
        dt_now = datetime.now()
        hours, minutes, seconds = dt_now.hour, dt_now.minute, dt_now.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as f:
            f.write(str(dt_now))
        print(dt_now, filename)
        sleep(1)


if __name__ == "__main__":
    main()
