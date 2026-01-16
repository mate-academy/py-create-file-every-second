
from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        filename = (f"app-{time_now.hour}_"
                    f"{time_now.minute}_"
                    f"{time_now.second}.log")
        with open(filename, "w") as file:
            file.write(str(time_now))
        print(f"{time_now} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
