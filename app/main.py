from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        hours = time.hour
        minutes = time.minute
        seconds = time.second

        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        file_a = open(file_name, "w")

        file_a.write(f"{time}")

        print(time, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
