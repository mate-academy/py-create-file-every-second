from datetime import datetime
from time import sleep


def create_file(name: str, current_time: str) -> None:
    with open(f"{name}.log", "w") as f:
        f.write(current_time)
        print(f"{current_time} {name}.log")


def main() -> None:
    while True:
        now = datetime.now()
        name = f"app-{now.hour}_{now.minute}_{now.second}"
        current_time = str(datetime.now())
        create_file(name, current_time)
        sleep(1)


if __name__ == "__main__":
    main()
