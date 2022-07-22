from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        x = datetime.now()
        with open(f"app-{x.hour}_{x.minute}_{x.second}.log", "w") as f:
            f.write(str(x))
        print(x, f"app-{x.hour}_{x.minute}_{x.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
