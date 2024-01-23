from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():

    while True:
        dt_string = datetime.now().strftime("%H_%M_%S")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sleep(1)
        with open(f"app-{dt_string}.log", "w") as f:
            f.write(timestamp)

        print(f"{timestamp} app-{dt_string}.log")


if __name__ == "__main__":
    main()
