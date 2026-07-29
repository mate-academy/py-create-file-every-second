from time import sleep
from _datetime import datetime


def main() -> None:

    while True:
        time_now = datetime.now()

        with open(f"app-{time_now.hour}_"
                  f"{time_now.minute}_"
                  f"{time_now.second}.log", "w") as file:
            file.write(str(datetime.now()))

            print(time_now, f"app-{time_now.hour}_"
                            f"{time_now.minute}_"
                            f"{time_now.second}.log")
            sleep(1)


if __name__ == "__main__":
    main()
