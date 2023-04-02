from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        name_file = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(name_file, "w") as f:
            f.write(str(now))
        print(f"{now} {name_file}")
        sleep(1)


if __name__ == "__main__":
    main()
