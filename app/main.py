from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now().replace(microsecond=0)
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log",
                  "w") as new_file:
            new_file.write(str(now))

        print(f"{now} app-{now.hour}_{now.minute}_{now.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
