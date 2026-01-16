from time import sleep
from datetime import datetime


def main() -> None:
    while True:

        with open(
                f"app-"
                f"{datetime.now().hour}_"
                f"{datetime.now().minute}_"
                f"{datetime.now().second}.log",
                "w"
        ) as f:

            content = str(datetime.now())
            print(content, f.name)
            f.write(content)

        sleep(1)


if __name__ == "__main__":
    main()
