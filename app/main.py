from datetime import datetime
from time import sleep


def main() -> None:

    while True:
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second
        full_time = current_time.isoformat(sep=" ", timespec="seconds")
        with open(f"app-{hour}_{minute}_{second}.log", "w") as file:
            file.write(full_time)

        print(f"{full_time} app-{hour}_{minute}_{second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
