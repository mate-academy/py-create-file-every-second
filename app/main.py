from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        result_file = open(f"app-{now.hour}_{now.minute}_{now.second}.log",
                           "w")
        result_file.write(f"{now.year}-{now.month}-{now.day}"
                          f" {now.hour}:{now.minute}:{now.second}")
        result_file.close()
        print(f"{now.year}-{now.month}-{now.day} {now.hour}"
              f":{now.minute}:{now.second}"
              f" app-{now.hour}_{now.minute}_{now.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
