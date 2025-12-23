import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current = datetime.now()
        file_name = f"app-{current.hour}_{current.minute}_{current.second}.log"

        with open(file_name, "w") as file:
            file.write(f"{str(current)}")

        print(f"{current} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
