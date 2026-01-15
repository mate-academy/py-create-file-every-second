from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        name = f"app-{now.hour:02d}_{now.minute:02d}_{now.second:02d}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {name}")

        sleep(1)


if __name__ == "__main__":
    main()
