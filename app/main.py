from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        hours, minutes, seconds = time_str.split(":")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as f:
            f.write(str(now))

        print(f"{now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
