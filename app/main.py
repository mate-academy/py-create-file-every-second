from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}"
        with open(f"{file_name}.log", "w") as f:
            f.write(f"{now}")
        print(f"{now} {file_name}.log")
        sleep(1)


if __name__ == "__main__":
    main()
