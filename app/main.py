from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        name = (f"app-{datetime.now().hour}_"
                f"{datetime.now().minute}_"
                f"{datetime.now().second}.log")
        with open(name, "w") as f:
            f.write(datetime.now().isoformat(" "))
        with open(name, "r") as f:
            print(f"{f.read()} {name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
