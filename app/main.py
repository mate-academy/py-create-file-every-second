import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        print(f"{datetime.now()} {file_name}")
        with open(file_name, "w") as file:
            file.write(f"{datetime.now()}")
        time.sleep(1)


if __name__ == "__main__":
    main()
