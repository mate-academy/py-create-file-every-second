from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        formatted = now.strftime("%H_%M_%S")
        name = f"app-{formatted}.log"
        with open(name, "w") as file:
            file.write(f"{now}")
            print(f"{now} {name}")
            sleep(1)


if __name__ == "__main__":
    main()
