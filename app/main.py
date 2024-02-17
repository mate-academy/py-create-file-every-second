from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        new_file = (f"app-{datetime.now().hour}"
                    f"_{datetime.now().minute}"
                    f"_{datetime.now().second}.log")
        with open(new_file, "w") as fl:
            fl.write(str(datetime.now()))
            print(f"{datetime.now()} {new_file}")

        sleep(1)


if __name__ == "__main__":
    main()
