import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        date_time = datetime.now()
        filename = \
            f"app-{date_time.hour}_{date_time.minute}_{date_time.second}.log"
        with open(filename, "w") as file:
            file.write(str(date_time))
            print(f"{date_time} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
