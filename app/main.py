from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        filename = datetime.now()
        with open(
                f"app-{filename.hour}_{filename.minute}_{filename.second}.log",
                "w"
        ) as f:
            f.writelines(str(filename))
        print(filename,
              f"app-{filename.hour}_{filename.minute}_{filename.second}.log"
              )
        sleep(1)


if __name__ == "__main__":
    main()
