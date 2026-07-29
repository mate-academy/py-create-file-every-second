from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hour = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        with open(f"app-{hour}_{minutes}_{seconds}.log", "w") as file:
            file.write(str(datetime.now()))
        print(
            f"{datetime.now()} {file.name}"
        )
        sleep(1)


if __name__ == "__main__":
    main()
