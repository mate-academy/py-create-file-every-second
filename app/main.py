from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        while True:
            hours = datetime.now().hour
            minutes = datetime.now().minute
            seconds = datetime.now().second
            now = str(datetime.now())
            file_name = f"app-{hours}_{minutes}_{seconds}.log"

            with open(file_name, "w") as f:
                f.write(now)

            print(f"{now} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
