from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        file = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(f"{file}", "w") as f:
            f.write(f"{now}")
        print(now, file)
        sleep(1)


if __name__ == "__main__":
    main()
