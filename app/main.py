from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:

        current = datetime.now()

        with open(
                f"app-{current.hour}_{current.minute}_{current.second}.log",
                "a"
        ) as f:
            f.write(f"{current}")
            print(f"{current} {f.name}")

        sleep(1)


if __name__ == "__main__":
    main()
