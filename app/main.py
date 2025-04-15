from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        name_of_file = (f"app-{time_now.hour}_"
                        f"{time_now.minute}_"
                        f"{time_now.second}.log")
        with open(name_of_file, "w") as f:
            f.write(f"{time_now}")
        print(f"{time_now} {name_of_file}")
        sleep(1)


if __name__ == "__main__":
    main()