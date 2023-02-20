import time
from datetime import datetime


def main() -> None:
    while True:
        name = (
            f"app-{datetime.now().hour}_"
            f"{datetime.now().minute}_"
            f"{datetime.now().second}.log"
        )
        text = datetime.now()
        with open(name, "w") as file:
            file.write(str(text))
        print(str(text) + " " + name)
        time.sleep(1)


if __name__ == "__main__":
    main()
