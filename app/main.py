from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w+") as f:
            f.write(f"{now}")
            f.seek(0)
            print(f"{f.read()} {f.name}")
        sleep(1)


if __name__ == "__main__":
    main()
