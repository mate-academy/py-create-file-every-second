from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        print(timestamp + " " + filename)

        with open(filename, "w") as new_file:
            new_file.write(timestamp)
        sleep(1)


if __name__ == "__main__":
    main()
