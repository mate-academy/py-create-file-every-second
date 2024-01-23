import time
from datetime import datetime


def main() -> None:
    while True:
        at_the_moment = datetime.now()
        time_str = at_the_moment.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (
            f"app-{at_the_moment.hour}_"
            f"{at_the_moment.minute}_"
            f"{at_the_moment.second}.log"
        )
        with open(file_name, "w") as f:
            f.write(time_str)
        print(f"{time_str} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
