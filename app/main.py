import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date_now = datetime.now()
        hours = date_now.hour
        minutes = date_now.minute
        seconds = date_now.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        line = str(date_now)
        print(line + " " + file_name)
        with open(file_name, "w") as f:
            f.write(line)
        time.sleep(1)


if __name__ == "__main__":
    main()
