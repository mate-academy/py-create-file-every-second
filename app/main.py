from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        current_timestamp = datetime.now()

        with open(file_name, "w") as f:
            f.write(str(current_timestamp))

        with open(file_name, "r") as f:
            print(f.read(), file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
