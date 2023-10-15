from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}_{datetime.now().minute}_"
                     f"{datetime.now().second}.log")
        with open(file_name, "a") as f:
            f.write(f"{datetime.now()}")
            print(str(datetime.now()) + " " + f.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
