import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        file_name = (f"app-{now.hour}_"
                     f"{now.minute}_"
                     f"{now.second}.log"
                     )
        with open(file_name, "w") as fl:
            fl.write(f"{now}")
            print(f"{now} {file_name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
