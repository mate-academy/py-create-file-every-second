from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import time


def main():
    while True:
        time_f = datetime.now()
        with open(f"app-{time_f}.log", "w") as fp:
            fp.write(str(time_f))

        print(f"{time_f} app-{time_f.strftime('%H_%M_%S')}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
