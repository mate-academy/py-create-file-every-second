from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        filename = (f"app-{datetime.now().hour}_{datetime.now().minute}_"
                    f"{datetime.now().second}.log")
        timestamp = datetime.now()
        with open(filename, "w") as f:
            f.write(str(timestamp))
        print(timestamp, filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
