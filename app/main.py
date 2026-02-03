from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")

        hours = now.hour
        minutes = now.minute
        seconds = now.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        print(f"{now_str} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
