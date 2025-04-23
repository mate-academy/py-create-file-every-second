import time
from datetime import datetime


def main() -> None:
    while True:
        data = datetime.now()
        name_file = f"app-{data.hour}_{data.minute}_{data.second}.log"
        with open(name_file, "w") as f:
            f.write(f"{data.date()} "
                    f"{data.strftime("%H:%M:%S")}")
            print(f"{data.date()} "
                  f"{data.strftime("%H:%M:%S")} {f.name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
