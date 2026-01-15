from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now().time()
        new_file = open(
            f"app-{time.hour}_{time.minute}_{int(time.second)}.log", "w"
        )
        new_file.write(f"{datetime.now()}")
        new_file.close()
        with open(new_file.name, "r") as f:
            print(f"{f.read()} {new_file.name}")
        sleep(1)


if __name__ == "__main__":
    main()
