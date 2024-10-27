from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        with (
            open(f"app-{date.hour}_{date.minute}_{date.second}.log", "w") as f
        ):
            f.write(str(date))
            print(f"{str(date)} {f.name}")
        sleep(1)


if __name__ == "__main__":
    main()
