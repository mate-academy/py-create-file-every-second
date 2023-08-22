from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    now = datetime.now()
    name = f"app-{now.hour}_{now.minute}_{now.second}.log"
    with open(name, "w") as f:
        f.write(str(now))
        print(now)
        print(name)


if __name__ == "__main__":
    while True:
        main()
        sleep(1)