from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():

    while True:
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second

        time_log = f"app-{hour}_{minute}_{second}.log"
        with open(time_log, "w") as f:
            time_now = datetime.now()
            f.write(f"{time_now}")
            print(time_now, f.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
