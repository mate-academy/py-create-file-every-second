from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        curr_time = datetime.now()
        file_name = (
            f"app-{curr_time.hour}_"
            f"{curr_time.minute}_"
            f"{curr_time.second}.log"
        )
        with open(file_name, "w") as f:
            f.write(str(curr_time))
            print(str(curr_time), f.name)
        sleep(1)


if __name__ == "__main__":
    main()
