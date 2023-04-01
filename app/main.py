from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        full_date_now = str(datetime.now())

        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        created_file = open(file_name, "w")
        created_file.write(full_date_now)
        print(full_date_now, file_name)
        created_file.close()

        sleep(1)


if __name__ == "__main__":
    main()
