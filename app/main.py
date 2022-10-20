from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        hours = str(datetime.now()).split()[1].split(":")[0]
        minutes = str(datetime.now()).split()[1].split(":")[1]
        seconds = str(datetime.now()).split()[1].split(":")[2].split(".")[0]
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(str(datetime.now()))
            print(f"{datetime.now()}" + " "
                  + f"app-{hours}_{minutes}_{seconds}.log")
        sleep(1)


if __name__ == "__main__":
    main()
