import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        v = datetime.now()
        with open(f"app-{v.hour}_{v.minute}_{v.second}.log", "w") as f:
            f.write(f"{v}")
            print(v, f"app-{v.hour}_{v.minute}_{v.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
