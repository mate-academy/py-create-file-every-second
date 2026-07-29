from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        dt = datetime.now()
        name = f"app-{dt.hour}_{dt.minute}_{dt.second}.log"
        with open(f"{name}", "w") as file:
            file.write(str(dt))
        print(f"{str(dt)} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
