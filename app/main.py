from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_string = str(datetime.now()).split()[1].split(".")[0]
        hours = time_string.split(":")[0]
        minutes = time_string.split(":")[1]
        seconds = time_string.split(":")[2]
        name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(name, "w") as f:
            f.write(str(datetime.now()).split(".")[0])

        with open(name, "r") as f:
            print(f"{f.read()} {name}")

        sleep(1)


if __name__ == "__main__":
    main()
