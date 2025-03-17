from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_file = datetime.now()
        filename = (f"app-{time_file.hour}_"
                    f"{time_file.minute}_{time_file.second}.log")

        with open(filename, "w") as file:
            file.write(str(time_file))

        print(time_file, filename)

        sleep(1)


if __name__ == "__main__":
    main()
