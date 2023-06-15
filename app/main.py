from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        with open(f"app-{current_time.hour}_{current_time.minute}_"
                  f"{current_time.second}.log", "a") as file:
            file.write(str(current_time))
            print(current_time, file.name)
        sleep(1)


if __name__ == "__main__":
    main()
