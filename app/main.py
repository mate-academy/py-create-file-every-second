from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        name = f"app-{date.hour}_{date.minute}_{date.second}.log"
        stamp = " ".join(date.isoformat().split("T"))

        with open(name, "w") as f:
            f.write(stamp)

        print(stamp, name)
        sleep(1)


if __name__ == "__main__":
    main()
