import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date = datetime.now()
        name = f"app-{date.hour}_{date.minute}_{date.second}.log"
        with open(name, "w") as f:
            f.write(f"{date}")
            print(f"{date} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
