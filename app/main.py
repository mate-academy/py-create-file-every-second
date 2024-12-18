from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current = datetime.now()
        log_name = f"app-{current.hour}_{current.minute}_{current.second}.log"
        with open(log_name, "a") as file:
            print(f"{current} {log_name}")
            file.write(f"{current}")
        sleep(1)


if __name__ == "__main__":
    main()
