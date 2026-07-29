from datetime import datetime
import time


def main():

    while True:
        h = datetime.now().hour
        m = datetime.now().minute
        s = datetime.now().second
        with open(f"app-{h}_{m}_{s}.log", "w") as f:
            f.writelines(f"{datetime.now()}")
            print(f"{datetime.now()} {f.name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
