from datetime import datetime
from time import sleep


def main():

    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        file_name: str = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(str(now))
            print(f"{now} {file_name}")
        sleep(1)

if __name__ == "__main__":
    main()
