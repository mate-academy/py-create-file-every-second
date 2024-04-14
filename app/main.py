from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        content = f"{now}"

        with open(filename, "w") as f:
            f.write(content)

        print(f"{now} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
