import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        name = datetime.now()
        fl = open(f"app-{name.hour}_{name.minute}_{name.second}" + ".log", "a")
        fl.write(f"{name}")
        fl.close()
        print(f"{name} app-{name.hour}_{name.minute}_{name.second}" + ".log")
        time.sleep(1)


if __name__ == "__main__":
    main()
