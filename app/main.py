import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w+") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
            f.seek(0)
            print(f"{f.read()} {f.name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
