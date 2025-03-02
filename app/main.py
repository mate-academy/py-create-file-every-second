from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    a = datetime.now()
    while True:
        name = f"app-{a.hour}_{a.minute}_{a.second}.log"
        with open(name, "w") as f:
            f.write(str(a))
            print(a, name)
            time.sleep(1)
            a = datetime.now()


if __name__ == "__main__":
    main()
