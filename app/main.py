from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        new_file = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(new_file, "w") as f:
            f.write(f"{datetime.now()}")

        print(f"{datetime.now()} {new_file}")
        sleep(1)


if __name__ == "__main__":
    main()
