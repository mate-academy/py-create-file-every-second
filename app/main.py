import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_now = datetime.now().time()
        name = f"app-{time_now.hour}_{time_now.minute}_{time_now.second}.log"
        date_now = datetime.now()
        with open(name, "w") as f:
            f.write(str(date_now))
        print(date_now, name)
        time.sleep(1)


if __name__ == "__main__":
    main()
