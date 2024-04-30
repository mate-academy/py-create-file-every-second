from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def create_file() -> str:
    now = datetime.now()
    filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
    content = str(now)
    with open(filename, "w") as f:
        f.write(content)
    print(f"{now} {filename}")


def main() -> None:
    while True:
        create_file()
        sleep(1)


if __name__ == "__main__":
    main()
