from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        with open(f"app-{datetime.now().hour}"
                  f"_{datetime.now().minute}"
                  f"_{datetime.now().second}.log",
                  "w") as file_name:
            file_name.write(str(datetime.now()))
            print(str(f"{datetime.now()} app-{datetime.now().hour}"
                      f"_{datetime.now().minute}"
                      f"_{datetime.now().second}.log"))
            sleep(1)


if __name__ == "__main__":
    main()
