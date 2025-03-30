from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        now = datetime.now()
        my_file = open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w")
        my_file.write(str(now))
        print(now, my_file.name)
        my_file.close()
        sleep(1)


if __name__ == "__main__":
    main()
