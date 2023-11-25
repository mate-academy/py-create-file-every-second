import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second

        current_time = datetime.now()

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(str(current_time))
            print(current_time, file.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
