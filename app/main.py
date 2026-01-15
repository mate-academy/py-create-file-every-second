import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        name = (f"app-{datetime.now().hour}_{datetime.now().minute}"
                f"_{datetime.now().second}.log")
        try:
            file_to_create = open(name, "x")
            file_to_create.write(str(datetime.now()))
            file_to_create.close()
        finally:
            print(datetime.now(), name)
            time.sleep(1)


if __name__ == "__main__":
    main()
