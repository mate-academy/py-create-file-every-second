import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(filename, "w") as file:
            file.write(str(datetime.now()))

        print(f"{datetime.now()} {filename}")

        time.sleep(1)
    pass


if __name__ == "__main__":
    main()
