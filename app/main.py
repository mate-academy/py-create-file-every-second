from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        our_time = datetime.now()
        name = f"app-{our_time.hour}_{our_time.minute}_{our_time.second}.log"
        timestamp = our_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
