import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        today = datetime.now()
        name = f"app-{today.hour}_{today.minute}_{today.second}.log"
        with open(name, "a") as f:
            f.write(str(today))
            print(today, name)
        time.sleep(1)


if __name__ == "__main__":
    main()
