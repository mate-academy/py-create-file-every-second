from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = str(datetime.now())
        name = date[11:19].replace(":", "_")
        with open(f"app-{name}.log", "w") as file:
            file.write(f"{date}")
        file.close()
        print(f"{date} app-{name}.log")
        sleep(1)


if __name__ == "__main__":
    main()
