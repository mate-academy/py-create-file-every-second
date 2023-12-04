from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second

        name_file = f"app-{hours}_{minutes}_{seconds}.log"
        with open(name_file, "w+") as file:
            file.write(f"{current_time}")
        print(datetime.now(), name_file)
        sleep(1)


if __name__ == "__main__":
    main()
