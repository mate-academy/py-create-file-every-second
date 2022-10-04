from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:

        time_now = datetime.now()
        hours = time_now.hour
        minutes = time_now.minute
        seconds = time_now.second

        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        print(time_now, file_name)

        with open(file_name, "w") as file:
            file.write(f"{time_now}")
        sleep(1)


if __name__ == "__main__":
    main()
