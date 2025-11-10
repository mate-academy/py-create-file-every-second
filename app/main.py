from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "w") as output:

            output.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}")

            print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {file_name}")

            sleep(1)


if __name__ == "__main__":
    main()
