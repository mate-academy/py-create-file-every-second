import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        t = datetime.now().time()
        d = datetime.now()
        with open(f"app-{t.hour}_{t.minute}_{t.second}.log", "w") as f:
            f.write(str(d))
        print(d, f"app-{t.hour}_{t.minute}_{t.second}.log")
        time.sleep(1)

if __name__ == "__main__":
    main()
