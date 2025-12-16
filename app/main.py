from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        datetime_now = datetime.now().isoformat().split("T")
        time_now = datetime_now[1].split(":")
        filename = f"app-{time_now[0]}_{time_now[1]}_{time_now[2]}.log"

        with open(filename, "w") as file:
            file.write(" ".join(datetime_now))

        print(" ".join(datetime_now), filename)
        sleep(1)


if __name__ == "__main__":
    main()
