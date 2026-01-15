from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        name = (f"app-{current_time.hour}_"
                f"{current_time.minute}_{current_time.second}.log")

        with open(name, "w") as f:
            f.write(str(current_time))
            print(f"{current_time} {name}")
            sleep(1)


if __name__ == "__main__":
    main()
