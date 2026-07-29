from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(filename, "w") as file:
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp)

        with open(filename, "r") as f:
            print(f"{f.read()} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
