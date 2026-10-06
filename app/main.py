from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hours, minutes, seconds = str(datetime.now()).split(":")

        if seconds[0] == "0":
            seconds = seconds[1]
        else:
            seconds = seconds[0: 2]
        if hours[-2] == "0":
            hours = hours[-1]
        else:
            hours = hours[-2:]
        if minutes[0] == "0":
            minutes = minutes[1]
        else:
            minutes = minutes[0: 2]

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(str(datetime.now()).split(".")[0])
            print(str(datetime.now()).split(".")[0]
                  + f" app-{hours}_{minutes}_{seconds}.log")
            sleep(1)


if __name__ == "__main__":
    main()
