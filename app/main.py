import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        with open(f"app-{datetime.now().hour}_{datetime.now().minute}_"
                  f"{datetime.now().second}.log", "w") as f:
            f.write(str(datetime.now()))
            print(str(datetime.now()) + f" {f.name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
