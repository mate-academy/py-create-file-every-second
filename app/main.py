from time import sleep
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        data = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w") as f:
            f.write(data)
            print(f"{data} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
