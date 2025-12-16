from datetime import datetime
from time import sleep


def main() -> None:
    try:
        while True:
            with open(f"app-{datetime.now().hour}_"
                      f"{datetime.now().minute}_"
                      f"{datetime.now().second}.log", "w") as new_file:
                new_file.write(f"{(datetime.now())}")

                print(f"{datetime.now()} "
                      f"app-{datetime.now().hour}_"
                      f"{datetime.now().minute}_"
                      f"{datetime.now().second}.log")
                sleep(1)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    main()
