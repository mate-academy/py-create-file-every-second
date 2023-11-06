from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        dt = datetime.now()
        with open(f"app-{dt.hour}_{dt.minute}_{dt.second}.log", "w") as file:
            file.write(str(dt))
        print(dt, f"app-{dt.hour}_{dt.minute}_{dt.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
