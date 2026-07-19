from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        filename = f"app-{now:%H_%M_%S}.log"

        with open(filename, "w") as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        print(now.strftime("%Y-%m-%d %H:%M:%S"), filename)

        sleep(1)


if __name__ == "__main__":
    main()
