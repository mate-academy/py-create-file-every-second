import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_date = datetime.now()
        name = (f"app-"
                f"{time_date.hour}_{time_date.minute}"
                f"_{time_date.second}.log"
                )
        with open(name, "w+") as f:
            f.write(time_date.strftime("%Y-%m-%d %H:%M:%S"))
            f.seek(0)
            print(f.read(), f.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
