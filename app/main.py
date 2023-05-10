from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        try:
            with open(
                    f"app-{datetime.now().hour}_"
                    f"{datetime.now().minute}_"
                    f"{datetime.now().second}.log", "x"
            ) as file:
                file.write(str(datetime.now()))
                print(
                    str(datetime.now()) + f" app-{datetime.now().hour}_"
                                          f"{datetime.now().minute}_"
                                          f"{datetime.now().second}.log"
                )
                sleep(1)
        except KeyboardInterrupt:
            raise KeyboardInterrupt


if __name__ == "__main__":
    main()
