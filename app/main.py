import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        time_file = open(file_name, "w")
        time_file.close()
        timestamp = datetime.now()
        with open(file_name, "w") as file:
            file.write(str(timestamp))

        print(f"{timestamp} {file_name}")
        time.sleep(1)
        pass


if __name__ == "__main__":
    main()
