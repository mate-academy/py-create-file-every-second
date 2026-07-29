import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(name, "w") as f:
            f.write(f"{now}")
        print(now, name)
        time.sleep(1)


if __name__ == "__main__":
    main()
