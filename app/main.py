import time
from datetime import datetime


def main() -> None:

    while True:
        file_contents = datetime.now()
        name = (
            f"app-{datetime.now().hour}_{datetime.now().minute}"
            f"_{datetime.now().second}.log"
        )
        with open(name, "w") as f:
            print(f"{file_contents} {name}")
            f.write(f"{file_contents}")
        time.sleep(1)


if __name__ == "__main__":
    main()
