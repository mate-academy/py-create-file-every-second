from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(f"{file_name}", "w") as fl:
            fl.write(f"{str(datetime.now())}")
        print(datetime.now(), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
