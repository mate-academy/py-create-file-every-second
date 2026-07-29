from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()  # сначала берём текущее время
        with open(f"app-{time.hour}_{time.minute}_{time.second}.log",
                  "w") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S"))
            print(time.strftime("%Y-%m-%d %H:%M:%S"), f.name)
        sleep(1)


if __name__ == "__main__":
    main()
