import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        file_name = (
            f"app-{datetime.now().hour}_{datetime.now().minute}_{datetime.now().second}.log"
        )
        with open(file_name, "a") as file:
            file.write(str(datetime.now()))
        print(datetime.now(), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
