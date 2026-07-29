from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        c_time = datetime.now()
        with open(
                f"app-{c_time.hour}_"
                f"{c_time.minute}_"
                f"{c_time.second}.log"
                , "w"
        ) as file:

            file.write(str(c_time))
            print(c_time, file.name)
            sleep(1)


if __name__ == "__main__":
    main()
