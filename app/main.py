from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        t = datetime.now()
        with open(f"app-{t.hour}_{t.minute}_{t.second}" + ".log", "w") as f:
            f.write(str(t))
            print(t, f"app-{t.hour}_{t.minute}_{t.second}" + ".log")
            time.sleep(1)


if __name__ == "__main__":
    main()
