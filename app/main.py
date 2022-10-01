import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        timestamp = datetime.now()
        file_name = timestamp.strftime("app-%H_%M_%S.log")

        with open(file_name, "a") as f:
            f.write(str(timestamp))

        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
