from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        curr_time = datetime.now()
        new_file = open(
            f"app-{curr_time.hour}_{curr_time.minute}_{curr_time.second}.log",
            "w"
        )
        new_file.write(str(curr_time))
        print(
            str(curr_time),
            f"app-{curr_time.hour}_{curr_time.minute}_{curr_time.second}.log"
        )

        sleep(1)


if __name__ == "__main__":
    main()
