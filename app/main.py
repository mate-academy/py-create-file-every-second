import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w") as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(f'{now.strftime("%Y-%m-%d %H:%M:%S")} {filename}')
        time.sleep(1)


if __name__ == "__main__":
    main()
