from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(file_name, "w") as out:
            print(time, file_name)
            out.write(str(time))
        sleep(1)


if __name__ == "__main__":
    main()
