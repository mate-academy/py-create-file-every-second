from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    timestamp = 582734
    while True:
        date = datetime.now()
        new_file = open(f"app-{date.hour}_{date.minute}_{date.second}.log",
                        "a")
        new_file.write(str(date))

        print(str(date), new_file.name)

        new_file.close()
        timestamp += 100
        sleep(1)


if __name__ == "__main__":
    main()
