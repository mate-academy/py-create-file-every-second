from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    # write your code here
    while True:

        i = datetime.now()
        name = f"app-{i.hour}_{i.minute}_{i.second}.log"
        with open(name, "a") as f:
            f.write(f"{datetime.now()}")
        print(datetime.now(), name)
        sleep(1)


if __name__ == "__main__":
    main()
