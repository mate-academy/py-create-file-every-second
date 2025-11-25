from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w") as f:
            f.write(f"{now}")
            print(f"{now} {f.name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
