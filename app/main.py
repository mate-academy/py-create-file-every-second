from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        time_str = time_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"app-{time_now.hour}_"
                  f"{time_now.minute}_"
                  f"{time_now.second}.log", "w") as fl:
            fl.write(time_str)
            print(time_str, fl.name)
        sleep(1)


if __name__ == "__main__":
    main()
