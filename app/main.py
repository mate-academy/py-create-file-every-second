from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        tims = datetime.now()
        file_name = f"app-{tims.hour}_{tims.minute}_{tims.second}.log"
        with open(file_name, "w") as log:
            log.write(tims.__str__())
        print(tims, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
