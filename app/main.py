from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = str(datetime.now()).split(":")
        hours = time[0][-2:]
        minutes = time[1]
        seconds = time[2][:2]

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(str(datetime.now()))
            print(str(datetime.now()), file.name)
        sleep(1)


if __name__ == "__main__":
    main()
