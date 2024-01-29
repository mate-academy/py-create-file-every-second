from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        date = datetime.now()
        filename = f"app-{date.hour}_{date.minute}_{date.second}.log"
        with open(filename, "w") as file:
            file.write(str(date))
            print(date, filename)
            time.sleep(1)


if __name__ == "__main__":
    main()
