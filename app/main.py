from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> any:

    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        current_date = datetime.now()
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as file:
            text = f"{current_date}"
            file.write(text)
            print(current_date, filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
