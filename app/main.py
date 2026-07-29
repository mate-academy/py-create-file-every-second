import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        curr_time = datetime.now().replace(microsecond=0)
        hours = curr_time.hour
        minutes = curr_time.minute
        seconds = curr_time.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(str(curr_time))
        print(f"{curr_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
