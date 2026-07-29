from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        ct = datetime.now()
        ct = str(ct)
        hours, minutes, seconds = ct[11:13], ct[14:16], ct[17:19]
        print(ct, end=" ")
        print(f"app-{hours}_{minutes}_{seconds}.log")
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(ct)
        sleep(1)


if __name__ == "__main__":
    main()
