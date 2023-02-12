from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        now = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        message = f"{now} {file_name}"
        with open(file_name, "w") as f:
            f.write(now)
            print(message)
            sleep(1)


if __name__ == "__main__":
    main()
