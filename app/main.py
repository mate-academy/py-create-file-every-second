from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        content = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(
                f"app-{time.hour}_{time.minute}_{time.second}.log", "w"
        ) as file:
            file.write(f"{content}")
        sleep(1)


if __name__ == "__main__":
    main()
