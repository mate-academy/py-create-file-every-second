from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        name_of_the_file = (f"app-{datetime.now().hour}_"
                            f"{datetime.now().minute}_"
                            f"{datetime.now().second}.log")
        time = datetime.now()
        with open(name_of_the_file, "wt") as f:
            f.write(str(time))
            print(time, name_of_the_file)

        sleep(1)


if __name__ == "__main__":
    main()
