from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        title = f"app-{hours}_{minutes}_{seconds}.log"
        with open(title, "w") as file:
            file.write(str(current_time))
        print(str(current_time), title)
        sleep(1)


if __name__ == "__main__":
    main()
