from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep

def main():
    while True:
        now = datetime.now()
        hours, minutes, seconds = now.hour, now.minute, now.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"{now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
