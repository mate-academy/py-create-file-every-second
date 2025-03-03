from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> any:

    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        with open(file_name, "r") as f:
            print(f.read(), file_name)

        sleep(1)


if __name__ == "__main__":
    main()
