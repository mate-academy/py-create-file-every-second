from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}_"
                     f"{datetime.now().minute}_{datetime.now().second}.log")
        with open(file_name, "w") as new_file:
            new_file.write(str(datetime.now()))
        print(datetime.now(), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
