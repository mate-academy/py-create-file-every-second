from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        name = (
            f"app-{datetime.now().hour}"
            f"_{datetime.now().minute}"
            f"_{datetime.now().second}.log"
        )
        with open(name, "w") as file:
            file.write(str(datetime.now()))
        print(f"{str(datetime.now())} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
