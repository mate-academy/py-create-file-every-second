from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour:02}_{now.minute:02}_{now.second:02}.log"
        with open(filename, "w") as file:
            file.write(str(now))
        print(f"{now} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
