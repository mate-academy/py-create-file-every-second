from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w") as f:
            f.write(str(now))
            f.close()

        file_ = open(f"app-{now.hour}_{now.minute}_{now.second}.log", "r")
        print(f"{file_.read()} app-{now.hour}_{now.minute}_{now.second}.log")
        f.close()
        sleep(1)


if __name__ == "__main__":
    main()
